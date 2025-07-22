import requests

def get_price(ticker):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ticker}&vs_currencies=usd"
    r = requests.get(url).json()
    return r[ticker]["usd"]
