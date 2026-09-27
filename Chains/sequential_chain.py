from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#  Create prompt1 
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

#  Create prompt2
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

#  Now Model from chatOpenAI()
model = ChatOpenAI()

# Agian parser -> strOutputParser()
parser = StrOutputParser()

# Now create chain 
chain = prompt1 | model | parser | prompt2 | model | parser

#  Invoke chain 
result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

# Analyse chain
chain.get_graph().print_ascii()

#  Now lets create a parallel chain