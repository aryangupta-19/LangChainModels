# LangChain Models Learning Setup

This repo is set up for learning LangChain chat models, prompts, embeddings, RAG, and agents step by step.

## Quick Start

```bash
cd /Users/aryangupta/Desktop/LangChainModels
source .venv/bin/activate
.venv/bin/python Setup/setup_check.py
```

Run the working Hugging Face chat model example:

```bash
.venv/bin/python ChatModels/chatModel_hf_api.py
```

## Environment

Keep real secrets in `.env`. Do not commit `.env`.

If you need a fresh template:

```bash
cp Setup/.env.example .env
```

For Hugging Face, use a User Access Token that starts with `hf_`:

```env
HF_TOKEN=hf_your_actual_token_here
```

For your OpenAI embeddings example, add:

```env
OPENAI_API_KEY=sk_your_actual_openai_key_here
```

Do not use S3 credentials like `AWS_ACCESS_KEY_ID` for LangChain chat model calls.

## Folder Roadmap

- `ChatModels/`: chat model examples
- `EmbeddedModels/`: embeddings and similarity
- `LLMS/`: plain text model calls
- `prompts_ui.py`: prompt templates and chat prompts
- `Setup/`: helper scripts, setup checker, docs, and env template

## Common Commands

```bash
.venv/bin/python Setup/setup_check.py
.venv/bin/python test.py
.venv/bin/python prompts_ui.py
.venv/bin/python ChatModels/chatModel_hf_api.py
.venv/bin/python EmbeddedModels/embedding_hf.py
Setup/run_hf_chat.sh
```

## Notes

The macOS `NotOpenSSLWarning` from `urllib3` is usually not the real crash. Focus first on clear errors like missing tokens, unauthorized API calls, or unsupported models/providers.
