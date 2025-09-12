from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()
model=ChatOpenAI(name='gpt-4.1-nano',temperature=0.7)

prompt = PromptTemplate(
    template='Suggest a catchy blog title about \n {topic}',
    input_variables=['topic']
)

topic = input("Enter the topic here:\n")

formatted_prompt=prompt.format(topic=topic)
response = model.invoke(formatted_prompt)


print(f"The title for your blog is {response.content}")
