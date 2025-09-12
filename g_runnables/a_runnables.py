from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI(name='gpt-4.1-nano')

template1=PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)
template2=PromptTemplate(
    template="Exaplin the following joke\n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain=RunnableSequence(template1,model,parser,template2,model,parser)
response = chain.invoke({"topic":"Black Holes"})
print(response)