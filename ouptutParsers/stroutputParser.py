from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate   # to make prompt dynamic 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# template 1) Detailed report on blackHole 
template1 = pormptTemplate(
    template="Write a Detailled report on {topic}",
    input_variables=['topic']
)

# template 2) Generate summary 
template2 = pormptTemplate(
    template="Write a 5 Line summary on the following text /n {text}",
    input_variables=['text']
)

# first send template 1 in prompt 
prompt1 = template1.invoke({'topic':'black hole'})
#invoke first prompt  
result = model.invoke(prompt1)

# now second template 
prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)

# this will give us normal response like final output will be 5 lines summary now we will rewrite this code with help of outputParser 
# in  