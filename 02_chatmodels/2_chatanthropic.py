from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
load_dotenv()
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
model = ChatAnthropic(model="claude-sonnet-4-20250514", api_key=CLAUDE_API_KEY)

result = model.invoke("Expain what is bubble sort")

print(result.content)