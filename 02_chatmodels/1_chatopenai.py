from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4.1-nano')

result = model.invoke("Explain GenAI in simple words?")

print(10*"--")
# print(result)
print(result.content)