from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(name="gpt=-4.1-nano")

template1=PromptTemplate(
    template='Generate a tweet about the topic {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

chain=RunnableParallel(
    {'tweet':RunnableSequence(template1,model,parser),
    "post": RunnableSequence(template2,model,parser)}
)

result=chain.invoke({"topic":"Role of Human in Agentic AI feedback"})
print(result)