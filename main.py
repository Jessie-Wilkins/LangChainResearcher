from langchain.agents import load_tools
from langchain.agents import get_all_tool_names
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

print(get_all_tool_names())

tools = load_tools(["bing-search", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("What is the Capital of Peru?")
