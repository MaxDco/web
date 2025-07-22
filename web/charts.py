import requests, datetime
import plotly.graph_objects as go

def fetch_history(ticker, days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{ticker}/market_chart?vs_currency=usd&days={days}"
    r = requests.get(url).json()
    prices = r["prices"]
    dates = [datetime.datetime.fromtimestamp(p[0] / 1000) for p in prices]
    values = [p[1] for p in prices]
    return dates, values

def build_plot_html(ticker):
    dates, values = fetch_history(ticker)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=values, mode='lines', name=ticker.upper()))
    fig.update_layout(title=f'{ticker.upper()} Price Chart', template='plotly_dark')
    return fig.to_html(full_html=False)
