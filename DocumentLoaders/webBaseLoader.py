from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/hyperlocal-preview-page?marketplace=HYPERLOCAL&originalUrl=%2Fpilgrim-australian-tea-tree-hair-shampoo-dandruff-itchy-scalp-men-women%2Fp%2Fitmd4f6d4c075583%3Fpid%3DSMPHFCK9GNNGFXH7%26lid%3DLSTSMPHFCK9GNNGFXH76BCYVR%26marketplace%3DHYPERLOCAL%26cmpid%3Dcontent_shampoo_8965229628_gmc&cmpid=content_shampoo_8965229628_gmc'
loader = WebBaseLoader(url)

docs = loader.load()
print(len(docs))    # single url ke liye single document ata hai , also we can pass multiple urls as list of urls
print(docs[0].page_content)


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))