from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", api_key=GEMINI_API_KEY)

result = model.invoke("Explain higgs bosons simply")

print(result.content)