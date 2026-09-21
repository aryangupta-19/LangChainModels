from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate   # to make prompt dynamic 
from langchain_core.output_parsers import StrOutputParser 
# note -> strOutput parser ka common usage ha chains ke sath (chains ki help se ham alag alag steps ko ik pipeline mai convert krskte hai)

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = pormptTemplate(
    template="Write a Detailled report on {topic}",
    input_variables=['topic']
)

template2 = pormptTemplate(
    template="Write a 5 Line summary on the following text /n {text}",
    input_variables=['text']
)

# First create a parser 
parser = StrOutputParser()

# Now make a chain -> pipeline where we will execute our whole flow template1 from user goes to model and parser will extract only text ignore metadata
# then paass this text to other model as template2 then parse it again where extract only summary ignore all the metadata
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})   # passing out topic

print(result)   # got same output 

# But this is the much easier way to perform same functionality 
# here we could have made chain without parser also but but that chain could go only upto model then extraction and other steps whould be explicit

# Therefore this is the main usage of stroutputParsers 
