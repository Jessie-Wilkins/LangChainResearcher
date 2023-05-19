from langchain.agents import load_tools, initialize_agent, AgentType
from LangChainResearcher.ExtraTools.FixedWriteFileTool import FixedWriteFileTool
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import ResearchAgentPrompt
from langchain.tools.file_management.read import ReadFileTool
from langchain.memory import ConversationBufferMemory


class ResearchAgentImpl:
    @staticmethod
    def Run(llm, query, format):
        llm = llm

        tools = load_tools(["ddg-search", "llm-math", "wikipedia"], llm=llm)

        tools.append(FixedWriteFileTool(root_dir="./output/"))

        tools.append(ReadFileTool())

        memory = ConversationBufferMemory()

        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory)

        prompt_template = ResearchAgentPrompt()

        prompt = prompt_template.PassInPromptInput(query, format)

        print(prompt)

        result =  agent.run(prompt)

        return result
