from langchain_huggingface import HuggingFaceembeddings
embedding=HuggingFaceembeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
docement=[
    "Gravitational waves are 'ripples' in space-time caused by some of the most violent and energetic processes in the Universe.",
    "A particle accelerator is a machine that uses electromagnetic fields to propel charged particles to very high speeds and energies to contain them in well-defined beams.",
    "Feynman was fond of saying that all of quantum mechanics can be gleaned from carefully thinking through the implications of this single experiment. He also proposed (as a thought experiment) that if detectors were placed before each slit, the interference pattern would disappear."
]
vector=embedding.embed_query(docement)

print(vector)