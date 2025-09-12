from altair import VariableParameter
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch,RunnableLambda
import os
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model = ChatOpenAI(name='gpt-4.1-nano')

parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")


parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

classifier_chain = prompt1|model|parser2

result= classifier_chain.invoke({'feedback':"This smartphone isn't smart"}).sentiment
print(result)
# print(result)
prompt2 = PromptTemplate(
    template="write and appropriate feedback for this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="write and appropriate feedback for this negetive feedback \n {feedback}",
    input_variables=['feedback']
)
branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2|model|parser),
    (lambda x:x.sentiment=='negative', prompt3|model|parser),
    RunnableLambda(lambda x:"could not find sentiment")
)

chain = classifier_chain|branch_chain

print(chain.invoke({'feedback':"This is a okayish phone"}))

chain.get_graph().print_ascii()