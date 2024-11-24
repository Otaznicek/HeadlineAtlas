from flask import Flask,render_template

app = Flask(__name__, template_folder='../web/templates')

@app.route("/")
def dashboard():
    return render_template("dashboard.jinja",long=48.7361,lat=16.6362)