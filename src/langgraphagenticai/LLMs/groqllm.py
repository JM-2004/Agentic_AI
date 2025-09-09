import os
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class GroqLLM:
    def __init__(self,user_contols_input):
        self.user_controls_input=user_contols_input

    def get_llm_model(self):
        try:
            #groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            groq_api_key=os.getenv("GROQ_API_KEY") 
            selected_groq_model=self.user_controls_input["selected_groq_model"]

            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Ocuured With Exception : {e}")
        return llm