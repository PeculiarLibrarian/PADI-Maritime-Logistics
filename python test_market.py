import ccxt

def observe_market():
    try:
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker('BTC/USDT')
        price = ticker['last']
        print(f"\n[BUREAU NOTIFICATION] Live BTC Price: ${price}")
    except Exception as e:
        print(f"\n[ERROR] Market observation failed: {e}")

if __name__ == "__main__":
    observe_market()

