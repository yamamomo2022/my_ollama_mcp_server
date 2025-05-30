from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int , b: int) -> int:
    """
    Adds two integers together.
    """
    return a + b

@mcp.tool()
def multiplay(a: int, b: int) -> int:
    """
    Multiplies two integers together.
    """
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
