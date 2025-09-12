from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text generation'
)
parser =JsonOutputParser()
model = ChatHuggingFace(llm=llm)
template = PromptTemplate(
    # template="Give me the name, age, and city of a fictional person \n {format_instruction}",
    # input_variables=[],
    # partial_variables={"format_instruction":parser.get_format_instructions()}
    template='Write 5 facts on {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={"format_instruction":parser.get_format_instructions()}

)
# prompt=template.format()
# print(prompt)
# result=model.invoke(prompt)

chain=template|model|parser
result=chain.invoke({"topic":"how gravity moves in space?"})

# final_result=parser.parse(result.content)
print(result)


# FLAW DOESNOT ENFORCE A SCHEMA
