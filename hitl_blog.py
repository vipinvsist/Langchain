from langgraph.graph import StateGraph, END
from typing import TypedDict
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# --- OpenAI client ---

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
# --- State Definition ---
class ArticleState(TypedDict):
    draft: str
    approved: bool
    feedback: str

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

def human_approval(state: ArticleState):
    decision = input("Approve article? (y/n): ").strip().lower()
    if decision == "y":
        state["approved"] = True
    else:
        state["approved"] = False
        state["feedback"] = input("Please provide feedback for revision: ").strip()
    return state

def revise_article(state: ArticleState):
    prompt = f"Revise the following article based on this feedback: '{state['feedback']}'\n\nArticle:\n{state['draft']}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    state["draft"] = response.choices[0].message.content
    print(f"\n[Agent] Revised Article:\n{state['draft']}\n")
    return state

def publish_article(state: ArticleState):
    print(f"[System] Publishing Article:\n{state['draft']}\n")
    return state

# --- HITL Workflow ---
def hitl_workflow():
    print("\n=== Human-in-the-Loop Publishing ===")
    builder = StateGraph(ArticleState)
    builder.add_node("generate", generate_article)
    builder.add_node("approval", human_approval)
    builder.add_node("revise", revise_article)
    builder.add_node("publish", publish_article)

    builder.set_entry_point("generate")
    builder.add_edge("generate", "approval")
    builder.add_conditional_edges(
        "approval",
        lambda state: "publish" if state["approved"] else "revise",
        {"publish": "publish", "revise": "revise"}
    )
    builder.add_edge("revise", "approval")
    builder.add_edge("publish", END)

    graph = builder.compile()

    # Save diagram
    with open("hitl_workflow.png", "wb") as f:
        f.write(graph.get_graph().draw_mermaid_png())

    graph.invoke({"draft": "", "approved": False, "feedback": ""})

if __name__ == "__main__":
    hitl_workflow()
