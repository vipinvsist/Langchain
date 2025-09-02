from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text generation'
)

model = ChatHuggingFace(llm=llm)
# model = ChatOpenAI(name='gpt-4.1-nano')
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

prompt1 = template1.invoke({'topic':"Warm holes"})
result1=model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})

result2 = model.invoke(prompt2)

print(result1.content)

print(20*"----")
print(result2.content)