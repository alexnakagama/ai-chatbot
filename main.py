from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_agent(model, tools)

    print("Welcome im your AI agent. Type 'quit' to exit.")
    print("You can ask me to perform calculations or simply chat with me!")
