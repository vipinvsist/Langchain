from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r"h_Rag_applications\document_loaders\dl-curriculum.pdf")
docs = loader.load()
print(docs[0].page_content)
print(100*"--")
print(docs[1].metadata)