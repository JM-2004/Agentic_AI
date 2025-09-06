from src.langgraphagenticai.state.state import State
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self, llm):
        self.llm = llm

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}

