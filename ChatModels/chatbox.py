import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def startChat():
    chat = client.chats.create(model="gemini-3.7-flash")
    print("Chat Started, Type exit to quit..!", flush=True)

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            
            # Use flush=True to ensure these print even if it crashes later
            print("1. Input received", flush=True)
            print("2. Sending to Gemini...", flush=True)
            
            response = chat.send_message(user_input)

            print("3. Response received!", flush=True)
            print("5. Gemini:", response.text, flush=True)

        except Exception as e:
            print(f"PYTHON ERROR: {e}", flush=True)

if __name__ == "__main__":
    startChat()