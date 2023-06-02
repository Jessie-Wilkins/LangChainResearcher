from langchain.chat_models import ChatOpenAI
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl

def main():
    llm = ChatOpenAI(temperature=0)
    ResearchAgentImpl.Run(llm, "What are the latest open source LLMs.", Format.LIST)

if __name__ == "__main__":
    main()