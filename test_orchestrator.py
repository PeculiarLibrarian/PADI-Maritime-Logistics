from uagents import Context, Model
from uagents.query import query

# Define the message structure (Matches your PADI standard)
class AuditRequest(Model):
    cargo_id: str
    status: str

# Your N-1-NODE Address from the earlier step
AGENT_ADDRESS = "agent1bace9fd22390e311136c4fd944aba882ce7443ff296dd0d5f120d8d650"

async def test_node():
    print(f"--- Initiating Orchestration Test for N-1-NODE ---")
    response = await query(destination=AGENT_ADDRESS, message=AuditRequest(cargo_id="NBO-MAR-001", status="Pending"))
    
    if response:
        print(f"Node Response: {response.decode()}")
    else:
        print("No response from node. Check if register_node.py is still running.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_node())
