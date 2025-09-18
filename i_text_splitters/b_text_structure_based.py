from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("h_Rag_applications\document_loaders\dl-curriculum.pdf")
# docs = loader.load()

text="""
Length-based text splitters are a fundamental tool in natural language processing (NLP) for dividing large blocks of text into smaller, more manageable chunks. This method operates by splitting the text based on a predefined character or token count, irrespective of the underlying semantic meaning or grammatical structure.
How They Work
The core principle is straightforward: you set a maximum length (e.g., 500 characters or 100 tokens), and the splitter divides the text into segments of that size. A common feature is the ability to define an overlap between chunks. This means a certain number of characters or tokens from the end of one chunk are repeated at the beginning of the next, which can help in preserving some contextual continuity.
For instance, if you have a 1200-character text and set a chunk size of 400 with an overlap of 50 characters, you would get chunks like this:
Chunk 1: Characters 1-400
Chunk 2: Characters 351-750
Chunk 3: Characters 701-1100
Chunk 4: Characters 1051-1200
Advantages of Length-Based Text Splitters
The primary benefits of this approach lie in its simplicity and predictability:
Simplicity and Speed: They are easy to implement and computationally efficient, making them suitable for processing large datasets quickly.
Consistent Chunk Sizes: This method guarantees that the resulting text segments will be of a uniform and predictable size, which can be crucial for models with strict input length limitations.
Control Over Output: You have direct control over the size of the output chunks, allowing for easy adaptation to the requirements of different models or applications.
Effectiveness with Unstructured Text: For text that lacks a clear and consistent structure, such as logs or raw data streams, length-based splitting can be a practical and effective solution.
Drawbacks of Length-Based Text Splitters
Despite their ease of use, length-based splitters have significant limitations, primarily related to their disregard for the linguistic structure of the text:
Loss of Semantic Context: The most significant drawback is the potential to break up semantically related content. A sentence, paragraph, or even a single word can be split across two different chunks, leading to a loss of meaning and context.
Sentence and Word Fragmentation: By splitting purely on length, these splitters can cut sentences in half or even break words apart. This can be detrimental to the performance of downstream NLP tasks that rely on coherent sentences.
Ignoring Document Structure: They do not take into account the natural structure of a document, such as paragraphs, headings, or lists. More sophisticated methods that recognize these structures often produce more meaningful and contextually relevant chunks.
Suboptimal for Many NLP Tasks: For applications like question answering, summarization, or retrieval-augmented generation (RAG), where preserving the semantic integrity of the text is paramount, length-based splitting can be a poor choice. The fragmented nature of the chunks can lead to inaccurate or irrelevant results.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    
)
result=splitter.split_text(text)                                #split_text(text)

print(result)