import importlib.util
import os
import platform
from pathlib import Path

from dotenv import load_dotenv


REQUIRED_PACKAGES = [
    "langchain",
    "langchain_core",
    "langchain_huggingface",
    "huggingface_hub",
    "dotenv",
]

OPTIONAL_PACKAGES = [
    "langchain_openai",
    "langchain_anthropic",
    "langchain_google_genai",
    "numpy",
    "sklearn",
]

ENV_KEYS = [
    "HF_TOKEN",
    "HUGGINGFACEHUB_API_TOKEN",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "GOOGLE_API_KEY",
]


def package_status(package_name):
    return importlib.util.find_spec(package_name) is not None


def mask_secret(value):
    if not value:
        return "missing"
    if len(value) <= 8:
        return "set"
    return f"{value[:4]}...{value[-4:]}"


def main():
    load_dotenv()

    print("LangChain learning environment check")
    print("=" * 40)
    print(f"Python: {platform.python_version()}")
    print(f"Project: {Path.cwd()}")
    print()

    print("Required packages")
    for package in REQUIRED_PACKAGES:
        status = "OK" if package_status(package) else "MISSING"
        print(f"- {package}: {status}")
    print()

    print("Optional packages")
    for package in OPTIONAL_PACKAGES:
        status = "OK" if package_status(package) else "missing"
        print(f"- {package}: {status}")
    print()

    print("Environment variables")
    for key in ENV_KEYS:
        print(f"- {key}: {mask_secret(os.getenv(key))}")
    print()

    hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if hf_token and hf_token.startswith("hf_"):
        print("Hugging Face token format: OK")
    else:
        print("Hugging Face token format: missing or invalid")
        print("Add HF_TOKEN=hf_your_actual_token_here to .env")


if __name__ == "__main__":
    main()
