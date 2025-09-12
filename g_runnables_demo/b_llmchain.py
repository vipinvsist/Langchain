from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(name='gpt-4.1-nano',temperature=0.5)

prompt = PromptTemplate(
    template="Give a catchy title for my blog\n {topic}",
    input_variables=['topic']
)

chain = LLMChain(llm=model, prompt=prompt)
topic = input("Enter the blog title\n ")
output=chain.run(topic)

print("Generate Blog Tile", output)