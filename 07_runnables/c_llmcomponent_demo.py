import random
class DemoLLM:
    def __init__(self):
        print("LLM Created")

    def predict(Self,prompt):
        response_list=[
            'Black holes have a high gravitational pull',
            'IPL is a cricket League',
            "AI stands from Artificial Intelligence"
        ]

        return {'response': random.choice(response_list)}
    
llm = DemoLLM()

print(llm)

print(llm.predict("What are Black holes"))



class DemoPromptTemplate:
    def __init__(self,template,input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict)
    

template = DemoPromptTemplate(
    template='Write on {length} report on this topic: {topic}',
    input_variables=['topic']


)

temp=template.format({'topic':"warm holes", "length":"detailed"})
print(temp)


print(llm.predict(prompt=temp))
