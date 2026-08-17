import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

print(
    "Token loaded:",
    os.getenv("HUGGINGFACEHUB_API_TOKEN") is not None
)


llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)