import langchain
print(langchain.__version__)

# python ChatModels/chatModel_hf_api.py



# Now talking about structured or unstructured outputs 
# structured -> gives data in a well defined fromat eg: json,  more infomative not only english response 

# Advantages of structured outputs: 
# Data Abstraction
# Api Building, flask and fastapi are used to build api
# Agents, note chatbox can only talk to us but agents can perform work for us, eg they can calculate complex operations for us 
  

# LLMs talk to human but don't provide structured outputs they provide just english text that was the reason they were not able to 
# integrate with databses or other systems  

# And we provided structred outputs to llm so that they can now contact with other systems also


# LLMs are of 2 types -> 
# 1) Generate By default structred outputs like openAi     «« with_structured_output ««
# 2) Can't generate     «« output parsers ««  classes which help to structure the unstructured outputs 

# Talking about type-1 first 

# here before invoking model we have to just call a function with_structured_output and specify dataformat  

# Here we will use TypedDict , Pydantic , json_schema

# TypedDict -> It is a way to define dict in python where we specify what key and values can exists, it helps to ensure 
# a dict follows a proper structure 

# go to strOutputTypedDict.py for more info ««««««««««««««««««««« 

# note here we don't have any gurantee that data comes with proper vaildations like though we specified summary should be string but it mayu not come as strin g alsp 
# therfore for that we will use pydantic

# Pydantic -> data validation and data parsing library for python , it ensures data is correct also used in fastapi while building apis 
# (must study pydantic)

# pydantic gives error if we try to break constraints 
# pydantic do type conversions means string - 32 ko 32 hi read krega if int type field hai 
# import EmailStr -> it auto validates email 

# Now lets implement this pydantic learning to strOutputswithTypedDict by replacing typedDict with pydantic 


# Json Schema -> used when project is made with multiple languages frontend js, backend python  as json is univeral data format 

# typedDict is used when we only need typed hints and no validations reqd or full project in single language 

# pydantic used when we need data constraints , also we have to send default vlaues but again full project must be single language

# Json Schema when operating with other languages also , need validations but don't want to import extra python libraries also json provides validations 

# json don't provide default values and auto typeCasting  


# Some things to remember
# 1) with_structured_output(method)    «««   json mode   (when output reqd in json format )      and         function calling (used when we are calling functions)

# for openAi function calling is mainly used but gemini claud supprts json mode 
# there are some models -> where no support of json mode and functn mode therefore they can't give structured output 

# recall tinyLama model-> 
 

