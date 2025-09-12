from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Give a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Give a 5 point summary of the report given by the following \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

model = ChatOpenAI(name='gpt-4.1-nano')
chain = prompt1|model|parser|prompt2|model|parser

result = chain.invoke({'topic':"warmholes"})

print(result)


chain.get_graph().print_ascii()