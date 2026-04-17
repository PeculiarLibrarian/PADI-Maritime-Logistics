import ccxt
import statistics

def analyze_risk():
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    # Fetch 30 minutes of data for a better sample size
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=30)
    prices = [candle[4] for candle in ohlcv]
    
    current_price = prices[-1]
    avg = statistics.mean(prices)
    std_dev = statistics.stdev(prices)
    
    # Calculate Volatility as a percentage
    volatility_pct = (std_dev / avg) * 100
    
    print(f"\n--- Bureau Risk Report: {symbol} ---")
    print(f"Current Price: ${current_price:,.2f}")
    print(f"30-Min Average: ${avg:,.2f}")
    print(f"Volatility (StdDev): ${std_dev:.2f} ({volatility_pct:.4f}%)")
    
    if volatility_pct > 0.1:
        print("Market Condition: HIGH VOLATILITY (Exercise Caution)")
    elif volatility_pct < 0.02:
        print("Market Condition: COMPRESSED (Potential Breakout Imminent)")
    else:
        print("Market Condition: STABLE")

if __name__ == "__main__":
    analyze_risk()
