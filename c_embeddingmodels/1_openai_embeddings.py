from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions=64)
result = embedding.embed_query("Gravitational waves are 'ripples' in space-time caused by some of the most violent and energetic processes in the Universe.")
print(str(result))