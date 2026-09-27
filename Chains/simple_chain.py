# s1) prompt from user -> s2) send it to llm -> s3) response from llm to user 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# create prompt using prompt template 
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# create model passing nothing therefore any auto available model of OpenAi will be used 
model = ChatOpenAI()

# Then create a parser -> using stroutputParser here 
parser = StrOutputParser()

# Now linking them all using a chain 
chain = prompt | model | parser

# At Lst incoke chain using its topic 
result = chain.invoke({'topic':'cricket'})

print(result)

# Now we can also visualise our chain by printing it (use get_graph() and print_ascii() function )
chain.get_graph().print_ascii()


#  Now we will create a little complex chain -> calling llm two times 