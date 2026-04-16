import requests

# Configuration using the standard v1 endpoint
API_KEY = "PASTE_YOUR_NEW_OPENROUTER_KEY_HERE"
URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/PeculiarLibrarian", # Required by OpenRouter
    "X-Title": "PADI Nairobi Node"
}

data = {
    "model": "google/gemini-2.0-flash-001", # High-performance choice for PADI logic
    "messages": [
        {"role": "system", "content": "You are the PADI Global Settlement logic. Acknowledge the Sovereign Architect."},
        {"role": "user", "content": "Confirm Nairobi-01 Node active via v1 endpoint."}
    ]
}

try:
    response = requests.post(URL, headers=headers, json=data)
    if response.status_code == 200:
        print("\n🌐 BUREAU RESPONSE:")
        print(response.json()['choices'][0]['message']['content'])
    else:
        print(f"❌ CONNECTION FAILED: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"⚠️ LINK FAILURE: {e}")
