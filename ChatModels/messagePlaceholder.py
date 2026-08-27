from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),  # all past messages comes here 
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})
#chatHistory ki jgah placeholder mai chat_history.txt se bhejdiya purana chat and query mai apni new query send krdi 


print(prompt)