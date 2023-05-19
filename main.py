from langchain import OpenAI
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl

def main():
    llm = OpenAI(temperature=0)
    ResearchAgentImpl.Run(llm, "What are the latest open source LLMs.", Format.LIST)

if __name__ == "__main__":
    main()