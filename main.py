from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from dotenv import load_dotenv

from tools.calculator import sum
from tools.calculator import sub
from tools.calculator import div
from tools.calculator import mult

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = [sum, sub, div, mult]
    agent_executor = create_agent(model, tools)

    print("Welcome im your AI agent. Type 'quit' to exit.")
    print("You can ask me to perform calculations or simply chat with me!")

    while (True):
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssitant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()