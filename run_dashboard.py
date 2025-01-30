from flask import Flask
from backend.database import Database
from backend.dashboard import dashboard_app  # Importujte Blueprint správným názvem

# Inicializace aplikace Flask a MySQL
app = Flask(__name__)
Database.init_app(app)

# Registrace Blueprintu
app.register_blueprint(dashboard_app)

# Spuštění aplikace
if __name__ == "__main__":
    app.run(debug=True)
