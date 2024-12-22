from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

from dotenv import load_dotenv
from arduin_control import led_control

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)

def led_light_on() -> str:
    """
    Function called when user wants to turn on the LED.
    """
    return led_control('1')

def led_light_off() -> str:
    """
    Function called when user wants to turn off the LED.
    """
    return led_control('0')

tools = [led_light_on, led_light_off]
llm_with_tools = llm.bind_tools(tools)

sys_msg = SystemMessage(
    content="You are a helpful assistant, that can control a LED using my commands."
)

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)

# Add nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Add edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile()