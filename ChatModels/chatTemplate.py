# Open ai format 

from langchain_core.prompts import ChatPromptTemplate

# another way without using systemMessage , userMessage, aiMessage variables write like this 

# chatPromptTemplate -> Exactly same work as of promptTemplate to create dynamic templates 
# chatPromptTemplate used for multiple messgs while promptTemplate used for single msgs 
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

