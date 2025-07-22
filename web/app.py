from flask import Flask, render_template
from charts import build_plot_html
from prices import get_price

app = Flask(__name__)

@app.route('/')
def index():
    charts_html = {
        "DOGE": build_plot_html("dogecoin"),
        "SOL": build_plot_html("solana"),
        "XRP": build_plot_html("ripple")
    }

    prices = {
        "DOGE": get_price("dogecoin"),
        "SOL": get_price("solana"),
        "XRP": get_price("ripple")
    }

    return render_template("index.html", charts_html=charts_html, prices=prices)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
