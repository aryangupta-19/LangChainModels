from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('aryan_ai_assignment.pdf')

docs = loader.load()
# print(docs)

print(len(docs)) # ->  4 -pages in pdf therefore 4 pages 

print(docs[0].page_content)
print(docs[1].metadata)

# we have many other pdfLoaders eg: scanned pdf have their own good pdfLoader 