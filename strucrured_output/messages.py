from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(name='gpt-4.1-nano')

messages = [
    SystemMessage(content="You are an Physicst with deep knowledge about the quantum behaviour of the particles."),
    HumanMessage(content="Tell me how a quantum particle able to change its past?")
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)