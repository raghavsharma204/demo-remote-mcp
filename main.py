from fastmcp import FastMCP
import random
import json

# create the fastMCP instance
mcp = FastMCP("Simple Calculator Server")

#Tool - Add 2 numbers
@mcp.tool()
def add(a:int, b: int) -> int:
    """Add 2 numbers together
    Args:
        a (int): first number
        b (int): second number
        
        Returns:
            int: the sum of a and b"""
    return a+b

#Tool - generate a random number
@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 10) -> int:
    """Generate a random number between min_val and max_val
    Args:
        min_val (int): minimum value (default: 1)
        max_val (int): maximum value (default: 10)
        
        Returns:
            int: a random number between min_val and max_val"""
    return random.randint(min_val, max_val)

#Resource: server information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server"""
    info = {
        "name": "Simple Calculator Server",
        "description": "A simple server that can perform basic calculations and generate random numbers.",
        "version": "1.0.0",
        "tools": ["add", "random_number"],
        "author":"Raghav"
    }

    return json.dumps(info, indent=2)

#starting the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http", host = "0.0.0.0", port = 8000)




