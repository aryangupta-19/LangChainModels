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
# hamare nakliLLm nakliPromptTemplate yeh sb hai task runnable and then runnableConnector thha vo taskSpecific runnables ko connect kr rha thha therfore it was primitive runnable 

# Now we will study Runnable Primitives 
# 1st -> Runnable Sequence : connect two or more runnables sequentially into chains first's output = input of second (humara runnableConector yahi hai)

# lets generate a joke from a prompt 

# 2nd -> Runnable Parallels :Help to make parallel chains 

# topic ->  goes into  2 llms -> llm1 -> generate tweet on topic 
#                                     |
#                                    Generate a linkedin post on topic 
#  both llm get same input but generate different output 


# 3rd -> RunnablePassthrough -> jo input diya usi ko as it is output mai dedeta hai 

# 4th -> Runnable lambda -> can convert any python function to runnable -> now this function can make chain with other runnables.

# lets suppose 
# company database -> reviews -> llm -> tells sentiment 
# Realised reviews are not much clean they involve emojis, punctuations, smilies but ideally we should send clean data to llm 
# so create a function where we can do pre-processign -> remove emojis punctuations etc 
# now convert this function to a runnable using runnable lambda now we can directly connect its output to llm runnable then parser 


# Runnable branch 
# used to make conditionals chains -> ifelse for langchain


# LCEL -> Langchain Expression Language 
# note runnable sequence is used mostly in all cases -> therefore langchain reduced its structure 

# so now we can use pipe operator to write sequence 
# [r1 | r2 | r3 | r4]   runnable sequence can be wriiten using LCEL also 











# Now we will move towards Rag implementations
# Build Rag based application using langchain

# WE have already covered -> models prompts chains and runnables 

# RAG -> technique that combines info retrival with language generation -> where a model retrives relavent docuement from a knowledge base and then uses them as context to generate accurate and grounded response 

# In rag without uploading our document we can retrive data (privacy)
# No limit of document size  

# Now first we will study components of Rag-> document loaders , text splitters , vector databases , Retrivers 

 
#  In langchain we have 100s of document-loaders -> we will study mostly used document loaders -> TextLoader, PyPdfLoader, webLoader, CSVLoader

# Document Loaders -> data can be in different sources like pdf text cloud etc and we have to ensure that data come from any source , it should come in a specific format 
# here documets ke form mai ata hai in standardized form 

# Text-loader -> simplest loader converts text file into document object 

# Now lets use PyPdfLoader -> reads pdf files and converts it into documents 
# goes page by page in pdf and create document for each page 

# pyPdf uses internally PyPdf library to read pdf files -> simple files ke liye hai -> scanned pdf ke liye alag document-loaders hai 

# learnt -> how to load single text file or a pdf file -> but for multiple pdf or text files we will use directory_loader 
  

# WebBaseLoader -> Can load and extract content from a webPage, Internally uses 2 python libraries,  Request -> hhtp req to webpage and BeautifulSoup -> understands html structure and c onverts to text format 
# Works good with static webPages (html-heavy)
# SelniumURLoader -> works with js heavy also very vell 


# CSV LOADER -> Document Loader used to load csv files in langchain so that langchain can ask question to it 
# CSV = Comma-Separated Values.
# It makes document object for each row 


# We can also make custom document loaders -> where we will decide how load and lazy_load will work 



# Lets go with Text Splitters  -> If we have a large pdf (1000s of pages) -> it becomes to difficult to process this large pdf -> so we break it into chunks so that we can process small amount of data
# Articles, html , pdf, books -> break into chunks and then feed to llm -> reason -> llm has its own context length -> tells how much words or tokens llm can process at a time 

# reason 2 -> Text splitting gives best result in Embedding (converting text into vectors) , Semantic search -> query matching in vector embeddings (chunking again gives more precise searching), Summarization -> llm are great with chunks in summarization also
#  Optimise computational resources -> more memory efficient, parallel execution etc. 
 
# Length Based, Text Structure Based, Document Structure Based, Semantic Meaning Based.

# 1) Length Based Text Splitting -> phle se decide krlo chunks ka size kya hoga eg: 100 chars (simplest way), works faster
# DrawBack -> don't check linguistic structrue, grammar and semantic structure during text splitting -> some times it stops in between a word 


# 2) Text Structrue Based -> It says all texts follows some structure inheritly -> like paragraph wise text , then in paragraphs sentences , then in sentences words 
# We will study Reccurssive Character Text splitting (mostly used).
# Isme hum phle se seperators define krlete hai 
# eg: \n\n for paragraph , \n for line change, ' ' for spaces in words , '' chars.

# Recurssive -> First tries on the basis of paragraph then sentences then words then characters. 
# Yahan yeh words ko middle se split ne krta hierarchi may jata hai phle paragraph wise break if size greate than chunk size 
# then statement wise break again if size greater 
# then break words wise 
# if at any stage size goes lesser than chunk size it stops and make chunks so it can also make chunks whose length is less than decided chunk size so it avoides text splitting fromm middle 
# at last if chunk size is verysmall it will break on the basis of characters 


# Document-Structure Based
# When we have different type of texts -> like no proper hindi or no proper english but like a oops code file where we have calsses methods functions etc.

# Here it is not organised in paragraphs, sentences but in classes, functions etc 
# Again here we will use reccurssive text splitter but seprators are of different types :
# \nclass, \ndef, \n\tdef then normal \n\n, \n, " " "" .

# Same thing can also be applied to markdown text.


# There are some scenerios where both length_based and document-structure based text splitters fails eg: same paragraph mai different context ki battien hui hai 
# Semantic Meaning Based -> idea -> decision making is not based on length or structure but on semantic meaning 
# Semantic meaning -> tries to understand meaning of text and then tries to split on basis of meaning difference.







# Vector Stores in Langchain (very Important): Need 

# See in our FilFinder if someone is exploring some movie at last we can also show him a listing of similar movies to increase his engagemen on our website
# Now How to find movies which are similar to it for that we will use keyword matching -> like we can match generes , actors , Directors etc 

# If all these keywords matches, this means both movies are similar so we can add it to list of similar movies 

# but many times same actors directors do different storyline ki movies banate hai so yeh ik drawback hai 
# also some times alag alag actors directors genre ki movie with similar storyline hai toh yeh unko relate hi nai krpayga (drawback)

# So To make a better approach -> how to predict two movies are similar or not 

# We should compare plot of two movies here we will check storyline matchup. 
# But here we need plot of each movie -> find using apis or web scrapping.
# Now once we find all plots we have to make a system which will compare two plots and generate a similarity score -> higher the score higher is similarity

# But two text pieces ke semantic meaning ko compare karna hai -> very difficult   -> solved by deep learning 
# 
# Embeddings -> Technique which helps to represent semantic meaning of some text into numbers (vectors) 
# so we will create embedding vectors of each movie plot 
# Then finding similarities in numbers is easy 
# concept -> lets say vector embeddings generated for different plots are m1, m2, m3, m4 --- and so on 

# Now we will try to plot it in a cordinate system using vectors and try to finding angular distance in between -> so two vectors which have minimum relative angular distance will be identified as similar.

# Drawbacks  
# We have lakhs of movies -> so we have to create embeddin vector for each movie 
# storage -> we need proper storage for embedding vectors and main problem is we can't store embeddings vector in normal sql databases -> becoz if we store it there -> relational databases don't provide us comparisons features.
# Semantic Search -> We need similarities so we have to find cosine similarities -> also if we start comparing m1 with all other (lakhs) vectors it will take a lot of time and application will be slow -> so find smart way to reduce no. of camparisons.

# These 3 challenges are solved by vector stores.



# Vector store -> System designed to store and retrieve data represented as numerical vectors.

# 4 key features 
# 1) Storage -> vectors and associated metadata are reatained , vector stores gives 2 storage -> in Memory(ram) application off krne pr gayab or on disk (hard-drive) (consistant application reopen mai bhi chi rhenge)
# 2) Similarity Search -> We can compare given query vector with all available vectors 
# 3) Indexing -> Generally used to optimse searching -> Enables fast similarity searches on high dimential vectors.
# 4) CRUD Operations -> addign  new vectors , retrieve , delete etc 

# Indexing -> one way 
# lets suppse we have 10 lakh vector in vector store -> then it will make 10 clusters each containing one lakh vectors -> then it will find avg of each cluster at last it will get centroid of each cluster 
# now it will calculate similarity score of query vector and compare it with available clustre's centroid and easily find similar cluster then search in cluster -> therefore 10 lakh comparisons reduced to 1 lakh comparisons 
# This was the one way, there are a lot of another ways also.


# Usecases -> Recommendation system , Rag , Semantic Search , Image/Multimedia Searching

# Vector store -> storage + Retrivals (Similarity search)
# Now if we add other database features to vector store like -> Acid properties , Backups , Authentication, concurrency etc it will be a vector database. eg: qdrant, Pinecone
# In production Environment mostly databases are used.

# A vector database is afterall a vector store with extra features. but vice versa is not true



# Vector stores in Langchain:
# In langchain for all vector stores we have built-in components and all are designed on common interfaces eg we can easily replace FAISS with Chroma in future.


# Chroma DB-> It is a lightweight open-source vector databse that is friendly for local development and medium - scale production 
# Chroma can come between a vector store and vector databse (it have only few features of db features)

# check hierarchy of chroma db
# Tenant -> user creates multiple databses -> creates collections -> store multiple docs -> contains embedding vector + metadata of vector 

# Now we will code in google colab 
# first install all libraries 


from langchain.schema import Document

# Create LangChain documents for IPL players

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )


vector_store = Chroma(      # Creates new chroma db -> and sqlite3 file will be created where everything stores 
    embedding_function=OpenAIEmbeddings(),
    persist_directory='my_chroma_db',
    collection_name='sample'
)



# add documents
vector_store.add_documents(docs)
# For each document id is also generated 

vector_store.get(include=['embeddings','documents', 'metadatas']) # To check documents in vector db

# search documents
vector_store.similarity_search(
    query='Who among these are a bowler?',
    k=2
)

# search with similarity score  -> with each result, we will get score -> lesser score more similar as it is distance (representation) 
vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=2
)

# meta-data filtering   -> Adding filters on meta-data
vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"}
)


# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)

vector_store.update_document(document_id='09a39dc6-3ba6-4ea7-927e-fdda591da5e4', document=updated_doc1)\

# delete document
vector_store.delete(ids=['09a39dc6-3ba6-4ea7-927e-fdda591da5e4'])








# Retrivers in LangChain (IMP)

# It is a component in langchain that fetches relavent documents from a databse in response to a user's query

# {Data Source}  <--  Retriver (input -> user query)   --> document (output of retriever)
#                           |
#                          query

# There are multiple retrievers in langchain for different usecases 
# All retrievers are runnables (therefore they can be chainned and also pushed in existing chains)

# Types of Retrievers based on Data sources 

# Wikipedia Retriever -> Searches query on wikipedia 
# Vector store based retrievers -> Searches in vector databased 
# Archive Retriever -> Searches on Archive web-page.

# Types of Retrievers based on Search strategy

# MMR (Maximum Marginal Relevence)
# Multi-query Retriever 
# and more 

# Wikipedia Retriever: It is a retriever that queries wikipedia api to fetch content based on given query 
# sends query to wikipedia - api ---> retrieves most relevant articles ---> return them as langchain document objects 
# relevance is based on text matching 


retriever = WikipediaRetriever(top_k_results=2, lang="en")

# Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# Get relevant Wikipedia documents
docs = retriever.invoke(query)      # Invoke function also shows retriever is a runnable 

# This retriever doesnot load all articles of wikipedia and it performs searching in between and bring out only relavent documents.



# Vector store Retriever -> brings relavent documents from vector store (most common) based on semantic searching 
# documents stored in vector store (chroma) -> Each vector is converted to dense model using embedding model -->> user gives query -> query-> vector -> compare with available vectors and do semantic search 

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step 2: Initialize embedding model
embedding_model = OpenAIEmbeddings()

# Step 3: Create Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# Step 4: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})        # created retriever object , search_kwargs={"k": 2} tells how much responses we want 

query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# Remember same chiz hamne vectorSearch mai bhi kari thhi using similarity search why do we need retriver for that , becoz vector store searches only on the basis of one strategy, 
# And using retriever we can use different strategies for searching.

# Till now we only learnt simple retriever that's why we are not able to see difference, but we have other good retrievers also they can provide advanceed search strategies.
    
results = vectorstore.similarity_search(query, k=2)     

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
    

# Retrievers based on retrival strategy 

#  MMR -> maximum marginal relevance

# See problem faced by Programmars in MMR_PROB
# MMR solves this problem of redundancy -> How can we pick the result that are relavent to search query and different from eachother 

# Many times same info repeats -> MMR Reduces this problem -> next document is relavent + dissimilar to previous one 

