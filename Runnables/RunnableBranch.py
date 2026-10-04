# document -> llm -> summarise -> again check if summary > 500 words again ask llm to summarise 
# how to check len > 500 or not -> lambda x : len(x.split()) > 500 , chain 
# and if words less than 500 then simply runn runnablePassThrough and give output summary
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(       # first generating detailed report 
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(       # then summarizing generated report 
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser  # used LCEL expression 

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, prompt2 | model | parser),  # used LCEL expression 
    RunnablePassthrough()       # else case 
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)  # join both chain generation and branch chain where summarizing 

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))