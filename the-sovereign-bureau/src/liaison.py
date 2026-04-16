import requests
import json
import os
from pathlib import Path

# --- CONFIGURATION ---
GITHUB_USERNAME = "PeculiarLibrarian"
# On Free Tier, a PAT is highly recommended to reach the 5k rate limit.
# For now, we will try it without a token, or you can paste one below.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "") 

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "graph_data.json"

def fetch_repos():
    """Fetches public repositories for the Librarian."""
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Liaison Connection Failed: {e}")
        return []

def update_sovereign_graph():
    # 1. Load the existing "Hand-Crafted" Ontology first
    if DATA_PATH.exists():
        with open(DATA_PATH, 'r') as f:
            graph = json.load(f)
    else:
        graph = {"nodes": [], "links": []}

    # 2. Add a 'Sovereign Network' Anchor if it doesn't exist
    if not any(n['id'] == "Sovereign_Network" for n in graph['nodes']):
        graph["nodes"].append({"id": "Sovereign_Network", "group": "Object"})
        graph["links"].append({
            "source": "Nairobi_01_Node", 
            "target": "Sovereign_Network", 
            "label": "orchestrates"
        })

    # 3. Fetch Real-Time Repository Data
    print("📡 Liaison Agent: Dialing GitHub API...")
    repos = fetch_repos()
    
    for repo in repos:
        repo_name = repo["name"]
        
        # Avoid duplicates
        if not any(n['id'] == repo_name for n in graph['nodes']):
            # Add Repo as a Value Node (Gold)
            graph["nodes"].append({"id": repo_name, "group": "Value"})
            # Link it to the Network Object
            graph["links"].append({
                "source": "Sovereign_Network", 
                "target": repo_name, 
                "label": "manages"
            })

    # 4. Save the expanded Truth Source
    with open(DATA_PATH, 'w') as f:
        json.dump(graph, f, indent=4)
    
    print(f"✅ Success: {len(repos)} Repositories linked to the Sovereign Network.")

if __name__ == "__main__":
    update_sovereign_graph()