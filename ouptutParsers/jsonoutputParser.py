from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

# Whenever we use this jsonParser, we have to send additional instruction, which tells kind of output reqd from llm, and this instruction is given by parser when using get_format_instructions()
template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser   # template going to model then parser parsing it 

# result = chain.invoke({}) if nothing to send 
result = chain.invoke({'topic':'black hole'})

print(result)

# Note in json format structuring is not possible like here output is directly a list of facts we don't get any proper structrue of output 
# therefore the biggest drawback is that it can't enforce a schema 

# Therefore to enforce shema we have to use someother parser instead of jsonoutputParser 