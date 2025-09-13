from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnablePassthrough, RunnableSequence, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
load_dotenv()


model=ChatOpenAI(name="gpt=-4.1-nano")

template1=PromptTemplate(
    template='Generate detailed report on the {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Summarize the following text\n {text}',
    input_variables=['text']
)

parser=StrOutputParser()
report_chain=template1|model|parser

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300, template2|model|parser),        #    (condition, runnable)
    RunnablePassthrough()               # default
)

final_chain = report_chain|branch_chain


print(final_chain.invoke({'topic':"AI vs Human in jobs?"}))