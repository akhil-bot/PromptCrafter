import json
import ast
from langgraph.graph import StateGraph, END, START
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage
from models.openai_models import get_open_ai_json
# from langgraph.checkpoint.sqlite import SqliteSaver
from agents.Agents import (
    PromptWriterAgent,
    PromptReviewerAgent,
    EndNodeAgent
)
from states.state import AgentGraphState, get_agent_graph_state, state

def create_graph(server=None, model=None, stop=None, model_endpoint=None, temperature=0):
    graph = StateGraph(AgentGraphState)

    graph.add_node(
        "prompt_writer", 
        lambda state: PromptWriterAgent(
            state=state,
            model=model,
            server=server,
            stop=stop,
            model_endpoint=model_endpoint,
            temperature=temperature
        ).invoke(
            task=state["task"],
            # previous_plans=lambda: get_agent_graph_state(state=state, state_key="planner_all"),
            # prompt=mf_planner_prompt_template
        )
    )

    graph.add_node(
        "prompt_reviewer",
        lambda state: PromptReviewerAgent(
            state=state,
            model=model,
            server=server,
            stop=stop,
            model_endpoint=model_endpoint,
            temperature=temperature
        ).invoke(
            task=state["task"],
            prompt_writer_response=state["prompt_writer_response"]
        )
    )


    graph.add_node("end", lambda state: EndNodeAgent(state).invoke())

    # Define the edges in the agent graph
    def pass_review(state: AgentGraphState):
        review_list = state.get("router_response", "")
        if review_list:
            review = review_list[-1]
        else:
            review = "No review"

        if review != "No review":
            if isinstance(review, HumanMessage):
                review_content = review.content
            else:
                review_content = review
            
            review_data = json.loads(review_content)
            next_agent = review_data["next_agent"]
        else:
            next_agent = "end"

        return next_agent

    # Add edges to the graph
    graph.set_entry_point("prompt_writer")
    graph.set_finish_point("end")
    graph.add_edge(START, "prompt_writer")
    graph.add_edge("prompt_writer", "prompt_reviewer")
    graph.add_edge("prompt_reviewer", "end")


    return graph

def compile_workflow(graph):
    workflow = graph.compile()
    app = workflow
    from IPython.display import Image, display

    # display(Image(app.get_graph(xray=True).draw_mermaid_png()))
    return app
