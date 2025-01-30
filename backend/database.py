import json
from flask_mysqldb import MySQL
class Database:
    mysql = MySQL()

    @staticmethod
    def init_app(app):
        # Načtení databázové konfigurace z JSON
        try:
            with open("backend/db-config.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Soubor backend/db-config.json nebyl nalezen.")
            data = {}
        except json.JSONDecodeError:
            print("Chyba při dekódování JSON souboru.")
            data = {}

        # Konfigurace Flask aplikace
        app.config["MYSQL_HOST"] = data.get("host")
        app.config["MYSQL_USER"] = data.get("user")
        app.config["MYSQL_PASSWORD"] = data.get("password")
        app.config["MYSQL_DB"] = data.get("db")
        Database.mysql.init_app(app)

    @staticmethod
    def get_cursor():
        return Database.mysql.connection.cursor()
    @staticmethod
    def insert_articles(articles):
        query = """
        INSERT INTO articles (nazev_clanku, zdroj, zem_sirka, zem_vyska)
        VALUES (%s, %s, %s, %s)
        """
        try:
            cursor = Database.mysql.connection.cursor()
            for article in articles:
                cursor.execute(query, (
                    article['nazev_clanku'],
                    article['zdroj'],
                    article['zem_sirka'],
                    article['zem_vyska']
                ))
            Database.mysql.connection.commit()
            print(f"{len(articles)} článků bylo úspěšně vloženo do databáze.")
        except Exception as e:
            print("Chyba při vkládání článků do databáze:", str(e))
            Database.mysql.connection.rollback()

    @staticmethod
    def get_all_articles():
        """
        Načte všechny články z databáze.
        :return: Seznam slovníků s články
        """
        query = "SELECT nazev_clanku, zdroj, zem_sirka, zem_vyska FROM articles"
        try:
            cursor = Database.mysql.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            articles = [
                {
                    "nazev_clanku": row[0],
                    "zdroj": row[1],
                    "zem_sirka": row[2],
                    "zem_vyska": row[3]
                }
                for row in rows
            ]
            return articles
        except Exception as e:
            print("Chyba při načítání článků z databáze:", str(e))
            return []
