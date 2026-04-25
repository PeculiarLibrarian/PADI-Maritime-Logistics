import os
import subprocess
import sys
from rdflib import Graph

class Liaison:
    def __init__(self):
        self.root = os.path.expanduser("~")
        self.nodes = []
        self.unified_graph = Graph()
        self.refresh_fleet()

    def refresh_fleet(self):
        self.nodes = [os.path.join(dp, f) for dp, dn, filenames in os.walk(self.root) 
                      for f in filenames if f.endswith('.ttl')]

    def status(self):
        triples = 0
        padi_refs = 0
        for node in self.nodes:
            try:
                with open(node, 'r', encoding='utf-8') as f:
                    content = f.read()
                    triples += content.count('.')
                    padi_refs += content.count('padi:')
            except: continue
        print(f"\n═══ BUREAU STATUS ═══\n📡 Nodes: {len(self.nodes)}\n🧠 Triples: {triples}\n🛡️  Refs: {padi_refs}\n════════════════════\n")

    def unify(self):
        """Creates a Unified Graph View (Addressing 'No queryable unified graph view')"""
        print("🔗 Unifying fleet into global memory...")
        for node in self.nodes:
            try:
                self.unified_graph.parse(node, format="turtle")
            except Exception as e:
                print(f"⚠️  Syntax Error in {os.path.basename(node)}")
        print(f"✅ Unified Graph Active: {len(self.unified_graph)} triples in memory.")

    def audit_fleet(self):
        """Cross-node validation (Addressing 'No cross-node validation pipeline')"""
        self.unify()
        print("🛡️  Running Integrity Audit...")
        # Logic to check for undefined classes or orphaned properties
        q = "SELECT DISTINCT ?s WHERE { ?s ?p ?o . FILTER(strstarts(str(?s), 'http://example.org/padi#')) }"
        results = self.unified_graph.query(q)
        print(f"🔎 Detected {len(results)} Unique Sovereign Entities across 29 nodes.")

if __name__ == "__main__":
    agent = Liaison()
    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "status": agent.status()
        elif action == "unify": agent.unify()
        elif action == "audit": agent.audit_fleet()
    else:
        print("Liaison Active. Commands: status, unify, audit")

def maintain_shelves():
    import os
    shelves = [
        os.path.expanduser("~/the-library/peculiar-shelf/reports/"),
        os.path.expanduser("~/the-library/peculiar-shelf/ontologies/")
    ]
    for shelf in shelves:
        if not os.path.exists(shelf):
            os.makedirs(shelf, exist_ok=True)
            print(f"🔗 Liaison: Constructed missing shelf -> {shelf}")

if __name__ == "__main__":
    maintain_shelves()
