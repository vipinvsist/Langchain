from langchain_community.document_loaders import WebBaseLoader
import requests
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(name='gpt-4.1-nano')
url="https://www.flipkart.com/apple-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly33hn-a/p/itmdc5308fa78421?pid=COMGFB2GMCRXZG85&lid=LSTCOMGFB2GMCRXZG855GPGWQ&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=en__4NpdvxC9c6V6D2rXYbR4o3j2EWbURfIi8ACqtIkwzFMuPk_pnf8Rnkba-itNm-U_zcMCBd4e2NxAaDxXs2U9_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=wixw1ia2sw0000001758164629355"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
loader = WebBaseLoader(url, header_template=headers)
docs = loader.load()
prompt=PromptTemplate(
    template="Answer the followinng questions \n {question} from the following text\n {text}",
    input_variables=['question',"text"]
)
parser = StrOutputParser()
text = docs[0].page_content
chain = prompt|model|parser
response = chain.invoke({'question':"what is discussed on here","text":text})


# docs = loader.load()
# print(len(docs))
# print(100*"-")

# print(docs[0].page_content)

# download chrome driver