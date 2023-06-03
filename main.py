from langchain.chat_models import ChatOpenAI
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl

def main():
    llm = ChatOpenAI(temperature=0)
    query = input("What is the topic you want to research: ")
    format_input = input("Do you want this in a LIST or a SUMMARY format: ")
    while (format_input.lower() != Format.LIST.value.lower() and format_input.lower() != Format.SUMMARY.value.lower()):
        format_input = input("Input was incorrect. You must type either LIST or SUMMARY for your answer. Which format do you want: ")
    
    format_enum = Format.LIST if format_input.lower() == Format.LIST.value.lower() else Format.SUMMARY

    ResearchAgentImpl.Run(llm, query, format_enum)

if __name__ == "__main__":
    main()