import importlib

research_agent_module = importlib.import_module("ResearchAgentImpl")

my_class = research_agent_module.ResearchAgentImpl

my_class.Run()


# from ResearchAgentImpl import ResearchAgentImpl

# ResearchAgentImpl.Run()