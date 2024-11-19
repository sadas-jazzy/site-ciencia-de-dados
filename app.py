from flask import flask, render_template

app = flask(__name__, template_folder ="sitenciencia/templates", static_folder = "siteciencia/static")

@app.route("/")
def index():
    #return "<h1>Bom dia, professor.</h1>"
    return render_template("index.html")

@app.route("/analise ")
@app.route("/analise/<usuario>")
def analise(usuario):
    return render_template("analise.html")

if __name__ == "__main__":
    app.run(debug=True)