from flask import flask, render_template

app = flask(__name__, template_folder ="sitenciencia/templates", static_folder = "siteciencia/static")

@app.route("/")
def index():
    #return "<h1>Bom dia, professor.</h1>"
    return render_template("index.html")