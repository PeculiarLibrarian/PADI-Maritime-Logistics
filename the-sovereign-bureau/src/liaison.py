import requests
import json
from pathlib import Path

# --- CONFIGURATION ---
GITHUB_USERNAME = "PeculiarLibrarian"
# Note: Use an environment variable for the token in production!
GITHUB_TOKEN = "your_github_token_here" 
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "graph_data.json"

def fetch_github_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(url, headers=headers)
    if response.status_status == 200:
        return response.json()
    return []

def build_network_of_sovereignty():
    # 1. Start with your existing PADI Core Nodes/Links 
    # (You can load your current graph_data.json here first to append to it)
    
    graph = {
        "nodes": [
            {"id": "Nairobi_01_Node", "group": "Subject"},
            {"id": "Sovereign_Network", "group": "Object"}
        ],
        "links": [
            {"source": "Nairobi_01_Node", "target": "Sovereign_Network", "label": "orchestrates"}
        ]
    }

    # 2. Fetch real-time data
    repos = fetch_github_repos()
    
    for repo in repos:
        repo_name = repo["name"]
        # Filter for relevant PADI-related repos if desired
        graph["nodes"].append({"id": repo_name, "group": "Value"})
        graph["links"].append({
            "source": "Sovereign_Network", 
            "target": repo_name, 
            "label": "contains"
        })

    # 3. Save to the Sovereign Data Sector
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(graph, f, indent=4)
    print(f"Successfully synchronized {len(repos)} nodes to the Network of Sovereignty.")

if __name__ == "__main__":
    build_network_of_sovereignty()