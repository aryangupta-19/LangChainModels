import langchain
print(langchain.__version__)

# python ChatModels/chatModel_hf_api.py



# Now talking about structured or unstructured outputs 
# structured -> gives data in a well defined fromat eg: json,  more infomative not only english response 

# Advantages of structured outputs: 
# Data Abstraction -> Showing only the essential information to the user while hiding the unnecessary implementation details.
# Api Building, flask and fastapi are used to build api
    
# Agents, note ->  chatbox can only talk to us but agents can perform work for us, eg: they can calculate complex operations for us. 
  

# LLMs talk to human but don't provide structured outputs they provide just english text that was the reason they were not able to 
# integrate with databses or other systems  

# And we provided structred outputs to llm so that they can now contact with other systems also


# LLMs are of 2 types -> can and can't 
# 1) Generate By default structred outputs like openAi     «« with_structured_output ««
# 2) Can't generate     «« output parsers ««  classes which help to structure the unstructured outputs 

# Talking about type-1 first 

# here before invoking model we have to just call a function with_structured_output and specify dataformat  

# Here we will use TypedDict , Pydantic , json_schema

# TypedDict -> It is a way to define dictionary in python where we specify what key and values can exists, it helps to ensure 
# a dictionary that follows a proper structure 

# go to strOutputTypedDict.py for more info ««««««««««««««««««««« 

# note here we don't have any gurantee that data comes with proper vaildations like though we specified summary should be string but it may not come as string also 
# therfore for that we will use pydantic

# Pydantic -> data validation and data parsing library for python, it ensures data is correct also used in fastapi while building apis 
# (must study pydantic)

# pydantic gives error if we try to break constraints 
# pydantic do type conversions also means string - 32 ko 32 hi read krega if int type field hai 
# import EmailStr -> it auto validates email 

# Now lets implement this pydantic learning to strOutputswithTypedDict by replacing typedDict with pydantic 

# Json Schema -> used when project is made with multiple languages frontend js, backend python  as json is univeral data format 

# typedDict is used when we only need typed hints and no validations reqd or full project in single language 

# pydantic used when we need data constraints, also we have to send default vlaues but again full project must be single language

# Json Schema when operating with other languages also, need validations but don't want to import extra python libraries also json provides validations 

# json don't provide default values and auto typeCasting  


# Some things to remember
# 1) with_structured_output(method)    «««   json mode   (when output reqd in json format)      and         function calling (used when we are calling functions)

# for openAi function calling is mainly used but gemini claud supports json mode 

# there are some models -> where no support of json mode and functn mode therefore they can't give structured output 
# here we use output parsers for structured outputs 




# Output Parsers -> classes written in langchain which help to work with any type of llm and produce structured outputs
# output parsers can work with both type of models  can and can't 

# String output parser 
# Json output parser 
# Structured output parser 
# Pydantic output parser 
 
#  1) strOutputParser -> Takes response of llm and convert it to string 

# Asking LLM to generate some text on topic blackhole -> then sending whole text to llm and asking to convert it to 5 lines or summarise it 
# first do it using result.content then stroutputParser 



# first stroutputParser.py generally used with chains 

# Next is jsonOutputParser -> it will ask llm to return resoponse as json format,  can't provide structrued output or can't provide schema to output 

# StructuredOutputParser -> here we provide schema to llm and llm returns response based on schema therefore we can enforce schema here 

# PydanticOutputParser -> it is a structruedoutputParser that uses pydantic model to enforce validations on schema when processing llm's response 
# Here during making schema we pass pydantic-object in place of schema in parser 


# There are many more parsers in documentation -> langchain.output.parsers 












# Lets Start Chains in Langchain
# Models (done) ---> prompts (done)  ---> structred outputs (done) + output parsers (done) ---> Chains  +  Runnables

# user -- prompt -> llm -> output  -> show to user (all can be done mannualy + by using chains)

# chains can connect all steps and can easily make the pipeline

# Chains can also make different structure of pipelines like linear, parallel, sequential chains

# Lets make our simple chain user-prompt -> llm -> respone -> user 

# Next is a little complex prompt -> topic -> llm (asking detailed report) -> again passing report to llm and asking 5 summary lines sequential_chain.py

# Now lets create a parallel chain -> user provides text (Explanation of some topic) -> from this generate notes + quiz -> show user combination of both notes and quiz 

# Now lets create a conditional chain -> here user will give some feedback on our product and our model will add sentiments to it -> currently we will only show sentiments back (pos or neg)

# Model will extract whether it is positive or negatice 
# Now based on sentiment -> we will again send feedback to model and now ask it to generate response accordingly 







# Runnables in Langchain

# Runnables -> first note langchain is a framework used to contact different llm apis or models of different companies like gemini, claud, openchat, grok.

# Pdf-reader : pdf load -> split -> embed -> vector -> kernel -> llm -> parse.

# Till now we were manually creating prompt then manually pass prompt to llm and get reponse
# Now we are able to make chains -> joins 2 or more components 
# and most simplest chain is called as langchain -> llmchain here it will take prompt pass it to model and then give result in return.

# Retrival -> user-query -> search in vector database -> gives relevant text -> now make new prompt using relevant text and query => llm -> ans      This task is placed in all rag applications

# similarly langchain also created chain for Retrivals which are again and again used in rag, now this chain will ask for llm and retriver -> retriverQA chain

# overtime made too many chains -> which made its codebase much larger 
# now langchain had to make all components again so that all new components are standardised and can connect to eachother seamlessly and it is possible only with help of runnables 


# Runnable -> It is a unit of work, each runnale have some purpose -> takes input process it and gives output 

# -> Each runnable follows a common interface (each runnable have same set of methods)  eg: invoke() give input to runnable and then runnable give output, batch() takes multiple inputs and gives multiple outputs, stream() gives streaming o/ps

# -> We can connect all the runnables and can easily peroform complex functions also

# If we connect 2 runnables R1 and R2 then, output of R1 will work as input of R2 and it goes on 

# -> Whenever we connect runnabels to make a workflow, the workflow made is also a runnable and can be connected to other runnables.

# Therefore runnables follow 4 principles -> 1) Unit of work (i/p process o/p)  2) Common interface  3) We can connect runnables with eachother.  4) We can also connect two complex runnables with eachother.

# code on google colab.

# First lets make two classes -> 1) LLM-class - making llm component in langchain used by future users. eg: chatOpenAi(), genAi() these models calsses are already built and we just impoort and use them
# 2) Pompt template 


# import random
# class NakliLLM:
#     def __init__(self):           # initialisation constructor 
#         print("LLM Created")
        
#     def predict(self, prompt):     # predict -> for now giving anyone of response we created 
#         responseList = [
#             'Delhi is the capital of India',
#             'Virat kohli is my idol',
#             'Ai -> Artifical Intelligence'
#         ]
        
#         return {"reponse": random.choice(responeList)}
    
# llm = NakliLLM()
# LLM created
# llm.predict('What is the capital of India')
# {'response': 'AI stands for Artificial Intelligence'}   Response generated randomly
        


# Now Lets make class for PromptTemplate

# class NakliPromptTemplate:
#   def __init__(self, template, input_variables):
#     self.template = template
#     self.input_variables = input_variables

#   def format(self, input_dict):           # input_dict actually vo dictionary hai jo template ke placeholder ki values hold krti hai 
#     return self.template.format(**input_dict)




# ForExample: if my prompt looks like this

# prompt = NakliPromptTemplate(
#     template="My name is {name} and I am {age} years old.",
#     input_variables=["name", "age"]
# )

# then my input_dict would be like this.

# input_dict = {
#     "name": "Aryan",
#     "age": 21
# }




# template = NakliPromptTemplate(
#     template='Write a {length} poem about {topic}',
#     input_variables=['length', 'topic']
# )

# prompt = template.format({'length':'short','topic':'india'})


#  Now lets suppose i am an Engg and i have been provided with two llm classes NakliPrompt and NakliPromptTemplate and using these two I have to create a small LLM application where 
# I will ask topic from user and print poem on that topic (actually abhi asli poem nahi aygi but flow yahi hona chiye)


# llm = NakliLLM()  # First Create LLM

# prompt = template.format({'length':'short','topic':'india'})  then create prompt 

# llm.predict(prompt)    give poem as result 




# Now lets make a chain class (NakliLLMChains) which will, kind of chain these components means auto send prompt to nakliLLm

# class NakliLLMChain:
#   def __init__(self, llm, prompt):
#     self.llm = llm
#     self.prompt = prompt
#   def run(self, input_dict):
#     final_prompt = self.prompt.format(input_dict)     # input_dict will automatically trigger format function in nakliPromptTemplate class and give final_prompt
#     result = self.llm.predict(final_prompt)   # WE know result comes in form of dictionary lets extract string output of it 
#     return result['response'] 

# Now using NakliLLMChain class make same application 

# template = NakliPromptTemplate(
#     template='Write a {length} poem about {topic}',
#     input_variables=['length', 'topic']
# )

# llm = NakliLLM()

# chain = NakliLLMChain(llm, template)      # NakliLLMChain will chain llm and template 

# chain.run({'length':'short', 'topic': 'india'})

# At this point llm Team understood this chains are not flexible means (lets suppose we have to make 2 step chain -> eg: First generate joke then its application)
# Hence can't make 2 calls to llm using this chain therefore they are not much useful
# Main problem is due to -> see to interact with promptTemplate-class we need def format(): and for llm-Class we need def predict():

# We have to standarise these class by some method and then only we can make flexible chains 


# Lets make standardise components using runnables 

# Again reqd two classes NakliLLM, NakliPromptTemplate.

# First of all convert these both classes into runnables and all runnables must have common methos (imp -> invoke)

# How to make sure all classes have same methods -> Abstraction -> Recall abstract classes were the blueprints for classes they can't create objects but provide blueprint to derived classes and derived classes can create objects 

# Create Abstract class runnables then all component classes will inherit from runnable class and automatically all component classes will become runnables 

from abc import ABC, abstractmethod

class Runnable(ABC):      # This is an abstract class as inherit from ABC
    @abstractmethod
    def invoke(input_data):   # this method is abstract method 
        pass
        

import random

class NakliLLM(Runnable): # this is also runnable 

  def __init__(self):
    print('LLM created')
    
  def invoke(self, rompt):      # Jo kam phle predict kar rha thha ab invoke krr rha hai 
     
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

  def predict(self, prompt):        # Future mai isko remove krdenge 

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}


class NakliPromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
    
# Standardised both components next connect them and form chains -> Make a new class RunnableConnector -> This will help to chain two or more components now 

class RunnableConnector(Runnable):
    
    def __init__(self, runnableList):   # runnableList is list of runnable components eg prompt, llm
        self.runnableList = runnableList
        
    def invoke(self, inputdata):        # loop on prompt and llm -> first go on prompt and invoke it and get final prompt in inputdata and then invoke llm with inputdata that was output of previous step
        for runnable in self.runnableList:
            intputdata = runnavle.invoke(inputdata)
            
        return inputdata
            
# First create prompt 
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

# Now create llm 

llm = NakliLLM()
chain = RunnableConnector(template, llm)
chain.invoke({'length': 'long', 'topic': 'India'})

# Now here we can also connect more runnables like -> we can add strOutputParser component -> which finds string from output 
 class nakliStrOutput(Runnable):
    def __init__(self)
    
    def invoke(self, inputdata):
        return inputdata['response']  # inputdata se response key find krna hai 
    
# Add naklistroutputarser this before Runnableconnector

parser = NakliStrOutputParser()
# pass this parser in chain also
chain = RunnableConnector(template, llm, parser)


# Till now connected two or more runnables to make a chain now we will connect two chains to make a longer chain (4th principle)

# Chain1 -> generate Joke about a topic given in prompt
# chain2 -> input - joke -> then make explanation for the joke 

# Just create two prompt templates 1st -> write a joke about topic  and 2nd -> 

template1 = NakliPromptTemplate(
    template = "Write a joke about a {topic}",
    input_variables = ['topic']
)
template2 = NakliPromptTemplate(
    template = "Explain the following {response}",
    input_variables = ['response']
)

llm = NackliClass()
parser = NakliStrOutputParser()

# now create two chains 
chain1 = RunnableConnector([template1, llm]) # prints joke 
chain1.invoke('topic': 'AI')

chain2 = RunnableConnector([template2, llm , parser])   # generates explanation of joke
chain2.invoke('response': 'This is a Joke')

final_chain = RunnableConnector(chain1, chain2)
final_chain.invoke({'topic': 'Cricket'})


# Runnables -> 2 types -> task specific and primitive runnables 

# Task specific Runnables -> Core langchain components jinko hamne runnable mai convert kiya thha so that they can be used in pipelines  eg: chatOpenAi(), Retrival()

# Runnable primitves -> These are runnables jo dusre task speicif runnables ko connect krte hai 
# hamare nakliLLm nakliPromptTemplate yeh sb hai task runnable and then runnableConnector thha ik vo taskSpecific runnables ko connect kr rha thha therfore it was primitive runnable 

# Now we will study Runnable Primitives 
# 1st -> Runnable Sequence : connect two or more runnables sequentially into chains first's output = input of second (humara runnableConector yahi hai)

# lets generate a joke from a prompt 

# 2nd -> Runnable Parallels :Help to make parallel chains 

# topic ->  goes into  2 llms -> llm1 -> generate tweet on topic 
#                                     |
# #                                   Generate a linkedin post on topic 
#  both llm get same input but generate different output 


# 3rd -> Runnable pass through -> jo input diya usi ko as it is output mai dedeta hai 

# 4th -> Runnable lambda -> can convert any python function to runnable -> now this function can make chain with other runnables 
# lets suppose 
# company database -> reviews -> llm -> tells sentiment 
# Realised reviews are not much clean they involve emojis, punctuations, smilies but ideally we should send clean data to llm 
# so create a function where we can do pre-processign -> remove emojis punctuations etc 
# now convert this function to a runnable using runnablee lambda now we can directly connect its output to llm runnable then parser 


# Runnable branch 
# used to make conditionals chains -> ifelse for langchain


# LCEL -> Langchain Expression Language 
# note runnable sequence is used mostly in all cases -> therefore langchain reduced its structure 

# so now we can use pipe operator to write sequence 
# [r1 | r2 | r3 | r4]   runnable sequence can be wriiten using LCEL also 











# Now we will move towards Rag implementations