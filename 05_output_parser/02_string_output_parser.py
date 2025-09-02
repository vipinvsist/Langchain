# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-chat-v1.0",
#     task='text generation'
# )

# model = ChatHuggingFace(llm=llm)
model = ChatOpenAI(name='gpt-4.1-nano')
# 1st prompt template
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt template
template2 = PromptTemplate(
    template='Write a 5 line summary on the followint text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 |model |parser

result = chain.invoke({'topic':"Worm Holes"})
print(result)