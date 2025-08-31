from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions=64)
documnets = ["Gravitational waves are 'ripples' in space-time caused by some of the most violent and energetic processes in the Universe.",
    "A particle accelerator is a machine that uses electromagnetic fields to propel charged particles to very high speeds and energies to contain them in well-defined beams.",
    "Feynman was fond of saying that all of quantum mechanics can be gleaned from carefully thinking through the implications of this single experiment. He also proposed (as a thought experiment) that if detectors were placed before each slit, the interference pattern would disappear."
]

query = "Tell me about the gravitional waves?"
doc_embeddings = embedding.embed_documents(documnets)
query_embeddding = embedding.embed_query(query)

similarity = cosine_similarity([query_embeddding],doc_embeddings)[0]
print(sorted(list(enumerate(similarity)), key = lambda x:x[1])[-1])