from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,RunnablePassthrough, RunnableSequence, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
load_dotenv()


model=ChatOpenAI(name="gpt=-4.1-nano")

template1=PromptTemplate(
    template='Generate joke on the {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()
def word_conunt(text):
    return len(text.split())
chain1=RunnableSequence(template1,model,parser)

chain2=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "lenght": RunnableLambda(word_conunt)        # or lambda x:len(x.split())

    }
)

final_chain = RunnableSequence(chain1,chain2,)
result=final_chain.invoke({'topic':"AI"})
# print(result)

final_result = """{} \n word count  - {}""".format(result['joke'], result['lenght'])
print(final_result)