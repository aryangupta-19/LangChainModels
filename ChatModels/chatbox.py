import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def startChat():
    # chat = client.chats.create(model="gemini-3.7-flash")
    initial_history = []
    chat = client.chats.create(
        model="gemini-3.7-flash",
        history=initial_history
    )
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

# Now we can also add chat history so that model can recall things 
# Automatic Management: You do not need to manually append messages to a list. The chat object (created by client.chats.create) has a property called chat.history that grows automatically every time you call send_message.

# we can print whole history using this 
#             print("\n--- Full Conversation History ---")
            # for message in chat.history:
            #     role = message.role
            #     text = message.parts[0].text
            #    print(f"{role.upper()}: {text}")

# Till now we don't have any info about msgs title -> means msg sent by user or aibot

# TYpes of messages in langchain 
# system msgs,  Human msgs, Ai msgs 

# now implement ->  we will first define systemMessage in inital_history array

# Important note!! in open ai we have to maintain msgs mannualy and append in history but in gemini it creates a function 
# chat = client.chats.create(model="gemini-3.7-flash")
# this  chat is a function which maintains a record of past messages also 

# chat object conversation state maintain karta hai for subsequent calls, but initial_history list itself automatically 
# tumhari Python list ki tarah continuously update nahi hoti.

# Therefore in futute if we are going to make any chatbox using open ai api then we have to make all these 
# system_variable human_variable and ai_variable for messages storage


# Recall we learnt -> static vs dynamic prompts 
# static -> All control to user, mistypes can occur
# dynamic -> we provide placeholders to users to choose similar prompts or give 90 % of code and user can modify it 

# see for dynamic messages what we will do is 
# create a sytemMessage and humanMessage 
# -> systemMessage -> You are a helpful {domain} expert.    {domain} is a placeholder
# -> humanMessaege -> Explain about {topic}.
# these are some predefined messages 



# MESSAGE PLACEHOLDER -> special placeholder used to dynamically insert chatHistory or list of messages at run time 
# some times user does a chat with ai model and next day again comes and start from some incomplete topic
# now next day what aibot does -> declares chat template first ----> then loads chat history ------> then creat prompt 

#  Note in general we store ChatHistory in cloud database

