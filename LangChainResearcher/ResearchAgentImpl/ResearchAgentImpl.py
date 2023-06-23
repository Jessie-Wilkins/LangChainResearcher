from langchain.agents import load_tools, initialize_agent, AgentType
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import ResearchAgentPrompt
from LangChainResearcher.ExtraTools.OutputFormatter import OutputFormatter
from langchain.memory import ConversationBufferMemory


class ResearchAgentImpl:
    @staticmethod
    def Run(llm, query, format):
        llm = llm

        tools = load_tools(["ddg-search", "llm-math", "wikipedia"], llm=llm)

        tools.append(OutputFormatter())

        memory = ConversationBufferMemory()

        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory, handle_parsing_errors=True)

        prompt_template = ResearchAgentPrompt()

        prompt = prompt_template.PassInPromptInput(query, format)

        result =  agent.run(prompt)

        return result
