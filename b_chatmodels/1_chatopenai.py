from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4.1-nano',
                   temperature=0.3,
                   max_completion_tokens=50)

result = model.invoke("Explain GenAI in simple words?")

print(10*"--")
# print(result)
print(result.content)