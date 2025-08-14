from langgraph.graph import StateGraph, END
from typing import TypedDict
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# --- OpenAI client ---
client = OpenAI(api_key=OPENAI_API_KEY)  # Replace with your key

# --- State Definition ---
class ArticleState(TypedDict):
    draft: str

# --- Nodes ---
def generate_article(state: ArticleState):
    prompt = "Write a professional yet engaging 150-word article about Agentic AI."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    state["draft"] = response.choices[0].message.content
    print(f"\n[Agent] Generated Article:\n{state['draft']}\n")
    return state

def publish_article(state: ArticleState):
    print(f"[System] Publishing Article:\n{state['draft']}\n")
    return state

# --- Autonomous Workflow ---
def autonomous_workflow():
    print("\n=== Autonomous Publishing ===")
    builder = StateGraph(ArticleState)
    builder.add_node("generate", generate_article)
    builder.add_node("publish", publish_article)
    builder.set_entry_point("generate")
    builder.add_edge("generate", "publish")
    builder.add_edge("publish", END)

    graph = builder.compile()

    # Save diagram
    with open("autonomous_workflow.png", "wb") as f:
        f.write(graph.get_graph().draw_mermaid_png())

    graph.invoke({"draft": ""})

if __name__ == "__main__":
    autonomous_workflow()

