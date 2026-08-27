# TYpes of messages inlangchain 
# system msgm,  Human msgs, Ai msgs 

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = "You are a helpful assistant"
user_prompt = "Tell me about LangChain"

# Updated to gemini-3.6-flash as requested by the API error
chat = client.chats.create(
    model="gemini-3.6-flash",
    config={"system_instruction": system_prompt}
)

response = chat.send_message(user_prompt)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
    {"role": "model", "content": response.text}
]

print(messages)