import ccxt, statistics, json, os, time
from datetime import datetime

# CONFIGURATION: THE STRATEGIC MANDATE
P_FILE = 'portfolio.json'
START_BAL = 1000.0
USDT_BAL = 996.61

class SemanticEngine:
    """Interoperability Layer: Translates raw data into Shared Meaning"""
    @staticmethod
    def get_market_state(price, avg_p, vol_ratio, accel):
        if vol_ratio > 1.3 and accel and price > avg_p:
            return "VORTEX_EXPANSION"
        elif vol_ratio > 1.0 and not accel and price < avg_p:
            return "INSTITUTIONAL_DISTRIBUTION"
        elif vol_ratio < 0.3:
            return "LIQUIDITY_VACUUM"
        return "NEUTRAL_CHOP"

def load_p():
    if not os.path.exists(P_FILE):
        return {"balance_usdt": USDT_BAL, "balance_btc": 0.0, "high_water": 0.0}
    with open(P_FILE, 'r') as f: return json.load(f)

def run():
    ex = ccxt.binance({'enableRateLimit': True})
    p = load_p()
    tk = ex.fetch_ticker('BTC/USDT')
    cp = tk['last']
    
    # 1. RAW DATA INGESTION
    ohlcv = ex.fetch_ohlcv('BTC/USDT', '1m', limit=40)
    px = [c[4] for c in ohlcv]
    vx = [c[5] for c in ohlcv]
    avg_p, avg_v = statistics.mean(px[-30:]), statistics.mean(vx[-30:])
    
    # 2. SEMANTIC TRANSLATION
    vol_now = vx[-1] / avg_v
    vol_prev = vx[-2] / avg_v
    staircase = vol_now > vol_prev
    
    # Achieve Interoperability: Map raw data to the State Ontology
    state = SemanticEngine.get_market_state(cp, avg_p, vol_now, staircase)
    
    # 3. LOGIC GATES (Decoupled from raw data)
    is_entry = (state == "VORTEX_EXPANSION")
    
    if p['balance_btc'] > 0:
        p['high_water'] = max(p['high_water'], cp)
        # Strategic Exit: Trend break or 0.2% drop from high_water
        is_exit = (cp < p['high_water'] * 0.998) or (cp < avg_p)
    else:
        is_exit = False
        p['high_water'] = 0

    print(f"[{datetime.now().strftime('%H:%M')}] ${cp:,.2f} | STATE: {state} | Vol: {vol_now:.1f}x")

    # 4. EXECUTION LAYER
    if is_entry and p['balance_usdt'] > 10:
        p['balance_btc'], p['balance_usdt'] = p['balance_usdt'] / cp, 0
        p['high_water'] = cp
        print(f"==> SEMANTIC BUY TRIGGERED: {state} @ ${cp:,.2f}")
    elif is_exit and p['balance_btc'] > 0:
        p['balance_usdt'] = p['balance_btc'] * cp
        p['balance_btc'] = 0
        print(f"==> STRATEGIC EXIT @ ${cp:,.2f} | Bal: ${p['balance_usdt']:.2f}")
    
    with open(P_FILE, 'w') as f: json.dump(p, f)

if __name__ == "__main__":
    print("Nairobi-01 Elite v6.0: SEMANTIC INTEROP ACTIVE")
    while True:
        try: run()
        except Exception as e: print(f"Syncing... {e}")
        time.sleep(60)
