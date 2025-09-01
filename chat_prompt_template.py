from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
# or ChatPromptTemplate.from_messages
chat_template=ChatPromptTemplate(
    [
        ('system','You are a helpful {domain} expert'),
        ("human","Explain this {topic} from the {domain} in simple terms"),
        # SystemMessage(content='You are a helpful{domain} expert'),
        # HumanMessage(content='Explain this {topic} from the {domain} in simple terms')
    ]
)
prompt = chat_template.invoke({
    "domain":"Quantum Mechanics",
    "topic":"YDSE in quantum Mechanics"
})

print(prompt)