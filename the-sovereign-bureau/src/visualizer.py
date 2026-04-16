import os
import json
import streamlit as st
from pathlib import Path
from streamlit_agraph import agraph, Node, Edge, Config

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="PADI Sovereign Bureau", layout="wide")
st.title("🏛️ The Sovereign Bureau | Nairobi-01 Node")
st.markdown("### Living Library of Access | PADI Technical Standard v2.1")

# --- MULTI-SECTOR PATH DISCOVERY ---
# This ensures the cloud finds the data regardless of mounting point
current_dir = Path(__file__).resolve().parent
possible_paths = [
    current_dir.parent / "data" / "graph_data.json", # Relative to src
    Path("the-sovereign-bureau/data/graph_data.json"), # Relative to repo root
    Path("data/graph_data.json"),                      # Direct relative
]

data_path = None
for p in possible_paths:
    if p.exists():
        data_path = p
        break

# --- DATA LOADING & RENDERING ---
if data_path:
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # 1. SIDEBAR CONTROLS
    st.sidebar.header("Bureau Controls")
    show_labels = st.sidebar.toggle("Show Connection Labels", value=True)
    st.sidebar.info("Blue: Subjects | Gold: Values | Green: Objects")

    # 2. THE SOVEREIGN PALETTE
    color_map = {
        "Subject": "#1E90FF",  # Dodger Blue (Authority)
        "Value": "#FFD700",    # Gold (Information)
        "Object": "#32CD32"    # Lime Green (Classes/Ontology)
    }

    # 3. NODE & EDGE PREPARATION
    nodes = [
        Node(
            id=n["id"], 
            label=n["id"], 
            size=25, 
            color=color_map.get(n["group"], "#CCCCCC"),
            shape="dot"
        ) 
        for n in data["nodes"]
    ]

    edges = [
        Edge(
            source=e["source"], 
            target=e["target"], 
            label=e["label"] if show_labels else ""
        ) 
        for e in data["links"]
    ]

    # 4. CONFIGURATION (Physics & Aesthetics)
    config = Config(
        width=1000, 
        height=700, 
        directed=True,
        nodeHighlightBehavior=True, 
        highlightColor="#F7A7A7", 
        collapsible=False,
        physics=True,
        d3={
            "linkStrength": 0.2,
            "gravity": -400,      # Increased push for more breathing room
            "linkDistance": 180   # Longer connections for readability
        }
    )

    # 5. RENDER THE GRAPH
    agraph(nodes=nodes, edges=edges, config=config)

else:
    st.error("Sovereign Protocol Failure: graph_data.json not found in any known sector.")
    st.info(f"Scanning Root: {os.getcwd()}")
    st.info(f"Visible Sectors: {os.listdir('.')}")