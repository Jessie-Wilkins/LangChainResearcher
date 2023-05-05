from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI
from LangChainResearcher.ExtraTools.FixedWriteFileTool import FixedWriteFileTool
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import ResearchAgentPrompt, Format
from langchain.tools.file_management.read import ReadFileTool
from langchain.memory import ConversationBufferMemory


class ResearchAgentImpl:
    @staticmethod
    def Run(llm):
        llm = llm

        tools = load_tools(["ddg-search", "llm-math"], llm=llm)

        tools.append(FixedWriteFileTool(root_dir="./output/"))

        tools.append(ReadFileTool())

        memory = ConversationBufferMemory()

        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory)

        prompt_template = ResearchAgentPrompt()

        prompt = prompt_template.PassInPromptInput("Give me an extensive list of dishes from Peru and write it in a text document?", Format.LIST)

        result =  agent.run(prompt)

        return result
