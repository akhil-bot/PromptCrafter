from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

# Define the state object for the agent graph
class AgentGraphState(TypedDict):
    task: str
    prompt_writer_response: Annotated[list, add_messages]
    prompt_reviewer_response: Annotated[list, add_messages]


# Define the nodes in the agent graph
def get_agent_graph_state(state:AgentGraphState, state_key:str):
    if state_key == "prompt_writer":
        return state["prompt_writer_response"]
    elif state_key == "prompt_reviewer":
        return state["prompt_reviewer_response"]
    else:
        return None

    
state = {
    "task":"",
    "prompt_writer_response": [],
    "prompt_reviewer_response": [],
    "end_chain": []
}