from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('TextSplitters/aryan_ai_assignment.pdf')

docs = loader.load()    # hrr page ke according ik document mangwa liya 

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=12,       
    separator=''
)

result = splitter.split_documents(docs) # pass documents what we want to split 

print(result[0])

 # see overlap count makes character count in both chunks common -> 
    # like -> applications of AI techn{iques in} intelligent agent, 
    # these words in curly braces are counted in chunk 1 and 2 both 
    # chunk 1 -> applications of AI techniques in
    # chunk 2 -> iques in intelligent agent,
    
# This helps in reducing word middle splits and disadv -> it can also lead to more no. of chunks if overlab is higher
# Roughly overlap must be 10-12% of whole text.

