import time
import os
from padi_trade_engine import PADITradeEngine

def run_performance_bench():
    shapes = "PADI-Maritime-Logistics/maritime_governance.ttl"
    data = "PADI-Maritime-Logistics/vessel_data.ttl"
    
    engine = PADITradeEngine(shapes, data)
    
    print("\n" + "="*50)
    print("PADI TRADING ENGINE: HARDENED PERFORMANCE TEST")
    print("="*50)

    # TEST 1: COMPLIANT HIGH-VALUE TRADE
    start_time = time.time()
    res1 = engine.execute_trade("TRD-PERF-001", 1300000)
    end_time = time.time()
    print(f"⏱️ LATENCY (Compliant): {(end_time - start_time) * 1000:.2f} ms")

    # TEST 2: THE GHOST SHIP BREACH
    # We now force the Ghost Ship to claim to be a Vessel to trigger SHACL
    bad_data = "PADI-Maritime-Logistics/ghost_vessel.ttl"
    with open(bad_data, "w") as f:
        f.write("""
        @prefix ex: <http://example.org/padi#> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        ex:GhostShip a ex:Vessel . 
        # Missing vesselID - this must trigger failure.
        """)
    
    engine_fail = PADITradeEngine(shapes, bad_data)
    
    print("\n" + "-"*30)
    print("[ACTION] Testing Hardened Breach Detection...")
    start_time = time.time()
    res2 = engine_fail.execute_trade("TRD-PERF-FAIL", 500000)
    end_time = time.time()
    print(f"⏱️ LATENCY (Breach Detection): {(end_time - start_time) * 1000:.2f} ms")

if __name__ == "__main__":
    run_performance_bench()
