import os
import json
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.title("The Sovereign Bureau | Nairobi-01 Node")

# Multi-sector path discovery
possible_paths = [
    "the-sovereign-bureau/data/graph_data.json",
    "data/graph_data.json",
    "../data/graph_data.json",
    "graph_data.json"
]

data_path = None
for p in possible_paths:
    if os.path.exists(p):
        data_path = p
        break

if data_path:
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Rendering Logic
    nodes = [Node(id=n["id"], label=n["id"], size=25, group=n["group"]) for n in data["nodes"]]
    edges = [Edge(source=e["source"], target=e["target"], label=e["label"]) for e in data["links"]]
    
    config = Config(width=700, height=500, directed=True, nodeHighlightBehavior=True)
    agraph(nodes=nodes, edges=edges, config=config)
else:
    st.error("Sovereign Protocol Failure: graph_data.json not found.")
    st.info(f"Directory Contents: {os.listdir('.')}")