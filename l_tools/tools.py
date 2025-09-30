from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools import ShellTool
search=DuckDuckGoSearchResults()
results = search.invoke("who won aisa cup 2025")
print(results)

shell_tool = ShellTool()
# output = shell_tool.invoke("whoami")
# print(shell_tool.run({"commands": ["echo 'Hello World!'", "time"]}))
output = shell_tool.invoke("ls")
print(output)