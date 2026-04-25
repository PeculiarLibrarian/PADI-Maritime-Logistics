    def perform_handshake(self, rdf_payload):
        print("🛰️ Initiating Asynchronous Handshake with Sentinel Gate...")
        
        # 🛡️ Add 'User-Agent' to bypass bot filters
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (PADI-Bureau-N1-Node; Linux x86_64)"
        }
        
        endpoints = [
            f"{self.gate_url}/call/predict",
            f"{self.gate_url}/gradio_api/call/predict"
        ]
        
        for endpoint in endpoints:
            try:
                print(f"📡 Attempting with Headers: {endpoint}")
                # Note the addition of 'headers=headers'
                response = requests.post(
                    endpoint, 
                    json={"data": [rdf_payload]}, 
                    headers=headers,
                    timeout=15
                )
                
                if response.status_code == 200:
                    event_id = response.json().get("event_id")
                    print(f"✅ Ticket Issued: {event_id}")
                    return event_id
                else:
                    print(f"⚠️ {endpoint} returned {response.status_code}")
                    # Log the server message if available to find the real error
                    print(f"📄 Server Response: {response.text[:100]}")
            except Exception as e:
                print(f"❌ Connection Error: {e}")
        
        return None

