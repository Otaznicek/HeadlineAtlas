from flask import Blueprint, render_template
from .database import Database

# Definice Blueprintu
dashboard_app = Blueprint("dashboard", __name__, template_folder="../web/templates")

@dashboard_app.route("/")
def dashboard():
    # Načtení všech článků z databáze
    articles = Database.get_all_articles()

    if articles:
        return render_template("dashboard.jinja", articles=articles)
    return "No articles found", 404
