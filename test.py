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
# 1) Generate By default structred outputs like openAi
# 2) Can't generate

# Talking about type 1 first 

# here before invoking model we have to just call a function with_structured_output and specify dataType 
