# lets go with joke example again 
# topic -> generate joke -> now diring joke printing (print total no. of joke words also) and generally llms are not good in this work of counting words so,
# first create prompt -> llm -> output -> parser -> now create a parallel chain 

# first chain mai runnablePassThrough se joke as it print krenge 
# second chain mai we will use runnableLambda (which will count words) and give no. of words 
# at last join both and generate result 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

load_dotenv()

def word_count(text):       # function to count no. of words and willbe converted to runnable using runnable lambda 
    return len(text.split())    # split will break the string on the basis of space and length will count total parts now

# runnable_word_counter = RunnableLambda(word_counter)
# print(runnable_word_counter.invoke("Hii, I am Aryan"))

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser) # Creating joke here 

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),      # to print joke as it is 
    'word_count': RunnableLambda(word_count)    # to count no. of words in joke 
})  

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)  # connect joke generation with parallel chain 

result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])     
# Joke nextline word_count 

print(final_result)