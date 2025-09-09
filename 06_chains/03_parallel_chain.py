from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
import os

load_dotenv()
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

model1 = ChatOpenAI(name='gpt-4.1-nano')

model2 = ChatAnthropic(model="claude-sonnet-4-20250514", api_key=CLAUDE_API_KEY)

prompt1= PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template="Give the 5 short question answer for the quiz from the following text\n {text} ",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and {quiz}.',
    input_variables=['quiz','notes']
)


parser = StrOutputParser()

#  Parallel Chain
paralle_chain = RunnableParallel({
    'notes': prompt1|model1|parser,
    'quiz': prompt2|model2|parser
})

merger = prompt3|model1|parser

chain = paralle_chain|merger

text = """
A black hole is an astronomical body so dense that its gravity prevents anything from escaping, even light. Albert Einstein's theory of general relativity predicts that a sufficiently compact mass will form a black hole.[4] The boundary of no escape is called the event horizon. In general relativity, a black hole’s event horizon seals an object’s fate but produces no locally detectable change when crossed.[5] In many ways, a black hole acts like an ideal black body, as it reflects no light.[6][7] Quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional to its mass. This temperature is of the order of billionths of a kelvin for stellar black holes, making it essentially impossible to observe directly.
Objects whose gravitational fields are too strong for light to escape were first considered in the 18th century by John Michell and Pierre-Simon Laplace. In 1916, Karl Schwarzschild found the first modern solution of general relativity that would characterise a black hole. Due to his influential research, the Schwarzschild metric is named after him. David Finkelstein, in 1958, first published the interpretation of "black hole" as a region of space from which nothing can escape. Black holes were long considered a mathematical curiosity; it was not until the 1960s that theoretical work showed they were a generic prediction of general relativity. The first black hole known was Cygnus X-1, identified by several researchers independently in 1971.[8][9]
Black holes typically form when massive stars collapse at the end of their life cycle. After a black hole has formed, it can grow by absorbing mass from its surroundings. Supermassive black holes of millions of solar masses may form by absorbing other stars and merging with other black holes, or via direct collapse of gas clouds. There is consensus that supermassive black holes exist in the centres of most galaxies.
The presence of a black hole can be inferred through its interaction with other matter and with electromagnetic radiation such as visible light. Matter falling toward a black hole can form an accretion disk of infalling plasma, heated by friction and emitting light. In extreme cases, this creates a quasar, some of the brightest objects in the universe. Stars passing too close to a supermassive black hole can be shredded into streamers that shine very brightly before being "swallowed."[10] If other stars are orbiting a black hole, their orbits can be used to determine the black hole's mass and location. Such observations can be used to exclude possible alternatives such as neutron stars. In this way, astronomers have identified numerous stellar black hole candidates in binary systems and established that the radio source known as Sagittarius A*, at the core of the Milky Way galaxy, contains a supermassive black hole of about 4.3 million solar masses.
"""

result = chain.invoke({"text":text})

chain.get_graph().print_ascii()