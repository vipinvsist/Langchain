from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()

chat_history=[
    SystemMessage(content='You are an helpful AI assistant'),
]
model = ChatOpenAI(name='gpt-4.1-nano')
while True:
    user_input =  input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)


print(chat_history)
