from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode
import os
from dotenv import load_dotenv
load_dotenv()

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    tools=[TavilySearch(api_key=tavily_api_key,max_results=2)]
    print ("Tools Loaded: ",tools)
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)