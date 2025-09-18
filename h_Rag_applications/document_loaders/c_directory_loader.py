from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    pathh=r"books",
    glob=".pdf",
    loader_cls=PyPDFLoader
)

# docs = loader.load()
docs = loader.lazy_load()

print(len(docs))

# print(docs[324].page_content)
# print(docs[43].metadata)


for document in docs:
    print(document.metadata)