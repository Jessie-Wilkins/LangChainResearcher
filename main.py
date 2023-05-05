from langchain import OpenAI
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl

def main():
    llm = OpenAI(temperature=0)
    ResearchAgentImpl.Run(llm)

if __name__ == "__main__":
    main()