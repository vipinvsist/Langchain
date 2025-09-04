"""
Can enforce schema --> Biggest benifit
"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task='text generation'
)
model = ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name="fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3",description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template="Give 3 facts about the {topic} \n {format_instruction}",
    input_variables = ['topic'],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt =template.invoke({"topic":"How Black Holes and Warm Holes are connected"})

# result = model.invoke(prompt)

# final_result=parser.parse(result.content)

# print(final_result)

# With Chain
chain=template|model|parser

result=chain.invoke({'topic':"how em waves behaves in quantum world"})
print(result)

"""
Disadvantage:
    1. Data Vaildation
"""