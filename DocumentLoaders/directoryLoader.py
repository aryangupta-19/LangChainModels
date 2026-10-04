from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# dodcs = loader.load()  
docs = loader.lazy_load()\

for document in docs:
    print(document.metadata)
    
# Note -> it is taking a good amount of time to run the this program becoz we are loading these pdfs into memory (RAM) in future if we have 500 pdfs it becomes verydifficult 
# so langchain provide lazy_load -> Every document have its load function and lazy_load 
# load actually -> eager load -> loads everything then go forward 

# lazy_load -> loads on demand (phle ik load then remove and other loead)

# load -> when leser pdfs -> all needed at a time 
# lazy_load -> one at a time -> when amount of pdfs is larger 

