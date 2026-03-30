from langchain.tools import tool

# Tools for ai chatbot

@tool
def sum(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers, sums"""
    print("Tool has been called")
    return f"The sume of {a} and {b} is: {a+b}"

@tool
def sub(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers, substraction"""
    print("Tool has been called")
    return f"The substraction of {a} and {b} is: {a-b}"

@tool
def div(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers, division"""
    print("Tool has been called")
    if b < 0:
        print("You cannot divide by 0")
    return f"The result of {a} divided by {b} is: {a/b}"

@tool
def mult(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers, multiplication"""
    return f"The result of {a} multiplied by {b} is: {a*b}"