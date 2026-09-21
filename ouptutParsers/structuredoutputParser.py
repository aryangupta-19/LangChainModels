from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema # import note-> can't import from langchain_core 
# here we have to import it from langchain -> main liabrary -> langchain.output_parsers becoz langchain is overall library and core contains only reusable components and structrued output parser is not considered as much reusable 

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# First we have to create a schema which guide llm to to produce which kind of output 
# note here we create schema with help of ResponseSchema 
schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

# now create-out parser  
parser = StructuredOutputParser.from_response_schemas(schema)

# now make prompt 
template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',   # additional instructions -> that is format_instruction 
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'black hole'})
# result = model.invoke(prompt)
# finalResult = parser.parse(result.content)

# now we got a structrued output where all facts are arranged according to schema we specified 

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# Drawback -> we can only pass data but we can't provide data validatinos in structruedOutputParser 
# it can enforce schema but can't enforce validations 