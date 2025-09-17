from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    pathh=r"books",
    glob=".pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(len(docs))

print(docs[324].page_content)
print(docs[43].metadata)
