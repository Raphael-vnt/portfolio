from flask import Flask, render_template, request
from projets.jeux_de_hasard.blackjack.montecarlo import run_simulation
from projets.jeux_de_hasard.blackjack.resolution_analytique import get_W_0

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blackjack", methods=["GET", "POST"])
def blackjack():
    result = None
    W_0 = None
    W_0 = get_W_0()
    table_W_0 = W_0.to_html(classes="table table-striped")
    if request.method == "POST":
        n_games = int(request.form["n_games"])
        soft17 = request.form.get("soft17") == "on"
        result = run_simulation(n_games=n_games, soft17=soft17)
    return render_template("blackjack.html", result=result, table_W_0=table_W_0)

@app.route("/mlp")
def mlp():
    return render_template("mlp.html")

@app.route("/signal")
def signal():
    return render_template("signal.html")

if __name__ == "__main__":
    app.run(debug=True)
