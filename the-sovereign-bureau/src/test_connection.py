import os
from openai import OpenAI
from dotenv import load_dotenv

# Load Sovereignty Credentials
load_dotenv()

def verify_sovereignty():
    print("📡 Dialing OpenRouter Gateway via Universal Protocol...")
    
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    try:
        # Simple test: Ask the Librarian to identify itself
        response = client.chat.completions.create(
          model="google/gemini-2.0-flash-001", # High-efficiency model
          messages=[
            {"role": "user", "content": "Verify system status for the Nairobi-01 Node."}
          ]
        )
        print("✅ Success: OpenRouter Gateway is ACTIVE.")
        print(f"🤖 Response: {response.choices[0].message.content}")
        print("🏛️ Status: Sovereign Execution Layer is READY.")
    except Exception as e:
        print(f"❌ Error: Connection Failed. {e}")

if __name__ == "__main__":
    verify_sovereignty()
