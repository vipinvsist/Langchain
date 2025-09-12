from langchain_huggingface import HuggingFaceembeddings
embedding=HuggingFaceembeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text="Gravitational waves are 'ripples' in space-time caused by some of the most violent and energetic processes in the Universe.",
vector=embedding.embed_query(text)

print(vector)