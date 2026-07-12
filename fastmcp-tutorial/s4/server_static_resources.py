from pathlib import Path
from fastmcp import FastMCP
from fastmcp.resources import (
    TextResource,
    BinaryResource,
    FileResource,
    HttpResource,
    DirectoryResource,
)
from pydantic import AnyUrl

mcp = FastMCP("file-server")

# Text Resource
text_resource = TextResource(
    uri=AnyUrl("resource://hello"), name="Hello Resource", text="Hello from FastMCP"
)
mcp.add_resource(text_resource)

# Binary resource
binary_resource = BinaryResource(
    uri=AnyUrl("resource://binary"),
    name="Binary Resource",
    data=b"\x01",
    mime_type="application/octet-stream",
)
mcp.add_resource(binary_resource)

# File resource
example_file = Path("./feed.yaml").resolve()
# example_file.write_text("This text comes from a file - feed.yaml\n", encoding="utf-8")

file_resource = FileResource(
    uri=AnyUrl("resource://file"),
    name="Feed metadata",
    path=example_file,
    mime_type="text/yaml",
)
mcp.add_resource(file_resource)

# HTTP Resource
http_resource = HttpResource(
    uri=AnyUrl("resource://site"),
    name="Google's home page",
    url="https://www.google.com",
)
mcp.add_resource(http_resource)

# Directory Resource
data_dir = Path("./data").resolve()
data_dir.mkdir(exist_ok=True)
(data_dir / "a.txt").write_text("File A")
(data_dir / "b.txt").write_text("File B")

directory_resource = DirectoryResource(
    uri=AnyUrl("resource://data"), name="Data Directory", path=data_dir, recursive=False
)
mcp.add_resource(directory_resource)

if __name__ == "__main__":
    mcp.run()
