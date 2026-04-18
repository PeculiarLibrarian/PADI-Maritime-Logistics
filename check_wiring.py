import rdflib
from pyshacl import validate

# Direct Pathing to the Nairobi-01 Node
shapes_path = "PADI-Maritime-Logistics/maritime_governance.ttl"
data_path = "PADI-Maritime-Logistics/vessel_data.ttl"

try:
    shapes_graph = rdflib.Graph().parse(shapes_path, format="turtle")
    data_graph = rdflib.Graph().parse(data_path, format="turtle")

    conforms, _, results_text = validate(data_graph, shacl_graph=shapes_graph)

    if conforms:
        print("\n✅ WIRING SECURE: Nairobi-01 Node respects PADI Standard.")
    else:
        print("\n❌ GOVERNANCE BREACH: Unauthorized Data Structure.")
        print(results_text)

except Exception as e:
    print(f"⚠️ System Error: {e}")
