(The file `/media/devalex/DATOS1/repositorios/chat-bot/README.md` exists, but is empty)
# Chat-Bot: AI-Powered Conversational Agent

## Overview

This project is an interactive AI-powered chatbot built with Python, leveraging the LangChain framework and OpenAI models. The chatbot can perform basic arithmetic operations and engage in natural language conversations, acting as a simple AI agent that can both chat and solve math problems.

## Features

- **Conversational AI**: Chat with the bot using natural language.
- **Math Tools**: Perform basic arithmetic operations (sum, subtraction, division, multiplication) via built-in tools.
- **Extensible**: Easily add more tools or capabilities using the LangChain agent framework.

## How It Works

The chatbot uses LangChain's agent system to process user input. When a user asks a question or requests a calculation, the agent determines whether to respond conversationally or use one of the math tools. The tools are defined in `tools/calculator.py` and include sum, subtraction, division, and multiplication.


## Project Structure

- `main.py`: Entry point for the chatbot application.
- `tools/`: Directory containing tool modules used by the agent. For example:
	- `calculator.py`: Arithmetic tool functions.
	- `other_tools.py`: (Template for additional tools; extend as needed.)
- `pyproject.toml`: Project dependencies and metadata.
- `.env`: (Not included) Should contain your OpenAI API key and other environment variables.

## Getting Started

### Prerequisites

- Python 3.12+
- An OpenAI API key (set in a `.env` file)

### Installation

1. Clone this repository:
	```bash
	git clone <your-repo-url>
	cd chat-bot
	```
2. Create and activate a virtual environment (recommended):
	```bash
	python -m venv .venv
	source .venv/bin/activate
	```
3. Install dependencies:
	```bash
	pip install -r requirements.txt
	# or, if using pyproject.toml
	pip install .
	```
4. Create a `.env` file in the project root and add your OpenAI API key:
	```env
	OPENAI_API_KEY=your_openai_api_key_here
	```

### Running the Chatbot

Start the chatbot with:
```bash
python main.py
```

You will see a welcome message. Type your questions or math problems. Type `quit` to exit.

## Example Usage

```
Welcome im your AI agent. Type 'quit' to exit.
You can ask me to perform calculations or simply chat with me!

You: What is 5 + 7?
Assitant: The sume of 5 and 7 is: 12

You: Hello, who are you?
Assitant: I am your AI agent. How can I help you today?
```


## Extending the Bot

To add more tools, create new Python files in the `tools/` directory (e.g., `other_tools.py`) and define your tool functions there. Register new tools in the `tools` list in `main.py` to make them available to the agent.

## License

This project is licensed under the MIT License.
