from c_llmcomponent_demo import DemoLLM,DemoPromptTemplate
class DemoLLMChain:
    def __init__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt

    def run(self,input_dict):

        final_prompt=self.prompt.format(input_dict)
        result=self.llm.predict(final_prompt)
        return result['response']
    

template = DemoPromptTemplate(
    template='Write on {length} report on this topic: {topic}',
    input_variables=['topic','length'])

llm = DemoLLM()
print(llm)

chain=DemoLLMChain(llm=llm,prompt=template)

print(10*"========")
print(chain.run({'topic':"Black holes", "length":"detailed"}))