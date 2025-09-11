import random
from abc import ABC, abstractmethod

class Runnable:
    @abstractmethod
    def invoke(input_data):
        pass


class DemoLLM(Runnable):
    def __init__(self):
        print("LLM Created")

    def invoke(self,prompt):
        response_list=[
            'Black holes have a high gravitational pull',
            'IPL is a cricket League',
            "AI stands from Artificial Intelligence"
        ]
        return {'response': random.choice(response_list)}
        

    def predict(Self,prompt):
        response_list=[
            'Black holes have a high gravitational pull',
            'IPL is a cricket League',
            "AI stands from Artificial Intelligence"
        ]
        print("this method will be depricated")

        return {'response': random.choice(response_list)}
    

class DemoPromptTemplate:
    def __init__(self,template,input_variables):
        self.template = template
        self.input_variables = input_variables
    def invoke(self,input_dict):
        return self.template.format(**input_dict)
    
    def format(self,input_dict):
        print("This method will be depricated")
        return self.template.format(**input_dict)
    

class RunnableConnector(Runnable):
    def __init__(self,runnable_list):
        self.runnable_list=runnable_list

    def invoke(self,input_data):
        
        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)

        return input_data


class DemoStrParser(Runnable):
    def __init__(self):
        pass

    def invoke(self,input_data):
        return input_data['response']

template = DemoPromptTemplate(
    template='Write on {length} report on this topic: {topic}',
    input_variables=['topic','length']
    )

llm=DemoLLM()
parser=DemoStrParser()

chain=RunnableConnector([template,llm,parser])
result=chain.invoke({'topic':"Black holes", "length":"detailed"})


# print(result['response'])
# print(result)


template1=DemoPromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

template2=DemoPromptTemplate(
    template='Explain the following joke: {response}',
    input_variables=['response']
)

chain1=RunnableConnector([template1,llm])
result1=chain1.invoke({'topic':"AI"})
# print(result1)
chain2=RunnableConnector([template2,llm,parser])

final_chain=RunnableConnector([chain1,chain2])
final_chain_result=final_chain.invoke({'topic':"AI"})

print(final_chain_result)