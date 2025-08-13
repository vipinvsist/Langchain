from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm=OpenAI(model='gpt-4.1-nano')
result=llm.invoke("what is capital of india")
print(10*"--")
print(result)