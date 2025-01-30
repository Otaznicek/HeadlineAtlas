import requests
import json
from database import Database
from flask import Flask


app = Flask(__name__)
Database.init_app(app)

class Caller:
    def __init__(self):
        # Načtení seznamu zdrojů ze souboru sources.json
        with open("backend/sources.json", "r") as f:
            self.sources = json.loads(f.read())

    def call_webpilot(self):
        """
        Pošle jeden požadavek na WebPilot a zpracuje odpověď.
        """
        # Sestavení promptu
        prompt = (
            "Analyzuj HTML následujících domovských stránek zpravodajských webů:\n"
            f"{json.dumps(self.sources, indent=2)}\n\n"
            "Pro každou domovskou stránku:\n"
            "1) Najdi všechny články na titulní stránce.\n"
            "2) Pro každý článek získej jeho nadpis (title), krátký popis (pokud existuje) a URL článku.\n, zkus co nejvíc článků co můžeš"
            "3) Z nadpisu a popisu článku extrahuj geografická data:\n, zeměpisné údaje nesmí být null"
            "   - Hlavní lokaci, o které text pojednává (město nebo stát).\n"
            "   - Pokud jde o stát, použij souřadnice hlavního města.\n"
            "4) Vrať výsledek jako JSON pole, kde každý objekt má následující strukturu:\n"
            "{\n"
            '  "nazev_clanku": "Nadpis článku",\n'
            '  "zdroj": URL odkazu na článek",\n'
            '  "zem_sirka": (zeměpisná šířka, pokud nevíš tak hlavního města země), nesmí být null\n'
            '  "zem_vyska": (zeměpisná výška, pokud nevíš tak hlavního města země), nesmí být null\n'
            "}\n"
            "Nesmíš si vymýšlet žádná data. Použij pouze skutečné nadpisy, popisy a URL článků, které najdeš na stránkách. Nepiš mi nic jiného než ten json, absolutně nic jiného"
            
        )

        data = {"model": "wp-watt-3.52-16k", "content": prompt}
        headers = {"Authorization": "Bearer 1ee0e7cd5150414e8950d815292cc750"}

        rsp = requests.post("https://beta.webpilotai.com/api/v1/watt", json=data, headers=headers)
        if rsp.status_code != 200:
            print("[ERROR] WebPilot API response:", rsp.status_code, rsp.text)
            return []

        try:
            # Zpracování odpovědi
            response_json = rsp.json()
            raw_content = response_json.get("content", "").strip()
            print("[DEBUG] Raw response content:", raw_content)

            cleaned_content = raw_content.replace("```json", "").replace("```", "").strip()
            articles = json.loads(cleaned_content)
            
            valid_articles = []
            for article in articles:
                valid_articles.append({
                    "nazev_clanku": article.get("nazev_clanku", "Neznámý článek"),
                    "zdroj": article.get("zdroj", "Neznámý zdroj"),
                    "zem_sirka": article.get("zem_sirka"),
                    "zem_vyska": article.get("zem_vyska")
                })

            return valid_articles
        except (json.JSONDecodeError, KeyError) as e:
            print("[ERROR] Chyba při zpracování odpovědi WebPilot:", rsp.text)
            return []

    def call_and_store(self):
        """
        Zavolá WebPilot, získá články s geografickými údaji a uloží je do databáze.
        """
        articles = self.call_webpilot()
        if not articles:
            print("[INFO] WebPilot nevrátil žádná data.")
            return []

        # Vložení do databáze
        with app.app_context():
            Database.insert_articles(articles)
        print(f"[INFO] {len(articles)} článků bylo úspěšně vloženo do databáze.")
        return articles

# Spuštění procesu
caller = Caller()
caller.call_and_store()
