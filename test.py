import langchain
print(langchain.__version__)

# python ChatModels/chatModel_hf_api.py



# Now talking about structured or unstructured outputs 
# structured -> gives data in a well defined fromat eg: json,  more infomative not only english response 

# Advantages of structured outputs: 
# Data Abstraction
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

# Retrival -> user-query -> search in vector database -> gives relevant text -> now make new prompt using relevant text and query => llm -> ans      This task is placed in all rag application s

# similarly langchain also created chain for Retrivals which are again and again used in rag, now this chain will ask for llm and retriver -> retriverQA chain

# overtime made too many chains -> which made it codebase such larger 
# now langchain had to make all components again so that all new components are standardised and can connect to eachother seamlessly and it is possible only with help of runnables 


# Runnable -> It is a unit of work, each runnale have some purpose -> takes input process it and gives output 

# -> Each runnable follows a common interface (each runnable have same set of methods)  eg: invoke(), batch() takes multiple inputs and gives multiple outputs, stream() gives streaming o/p

# -> We can connect all the runnables and can easily peroform complex functions also

# If we connect 2 runnables R1 and R2 then output of r1 will work as input of r2 and it goes on 

# -> Whenever we connect runnabels to make a workflow, the workflow made is also a runnable and can be connected to other runnables.








