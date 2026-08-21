from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI tutor for a beginner learning LangChain."),
        ("human", "Explain {topic} in simple terms with one small example."),
    ]
)

messages = prompt.invoke({"topic": "prompt templates"})

print(messages)
