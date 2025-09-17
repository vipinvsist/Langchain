from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
loader = TextLoader(r"h_Rag_applications\document_loaders\poem.txt",encoding='utf8')  #loader
model=ChatOpenAI(name='gpt-4.1-nano')
prompt=PromptTemplate(
    template="write a summary of the poem: {poem}",
    input_variables=['poem']
)
parser = StrOutputParser()
poem=loader.load()

chain = prompt|model|parser
response = chain.invoke({"poem":poem})

print(response)
# print(type(poem))
# print(10*"=========")
# print(poem)

# print(len(poem))
# # print(type(docs[0]))

# print(poem[0].page_content)

print(poem[0].metadata)