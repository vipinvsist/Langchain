from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
load_dotenv()

model=ChatOpenAI(name="gpt=-4.1-nano")

template1=PromptTemplate(
    template='Generate joke on the {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Give an explanation for the {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
chain1=RunnableSequence(template1,model,parser)
chain=RunnableParallel(
    {'joke':RunnablePassthrough(),
    "explain": RunnableSequence(template2,model,parser)}
)

final_chain=RunnableSequence(chain1,chain)
result=final_chain.invoke({"topic":"black holes"})
print(result)