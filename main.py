from langchain.chat_models import ChatOpenAI
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl
from LangChainResearcher.ExtraTools.OutputFormatter import OutputFormatter
import streamlit as st

def main():
    llm = ChatOpenAI(temperature=0)
    query = st.text_input("What is the topic you want to research?")
    format_input = st.selectbox("Do you want this in a LIST or a SUMMARY format?", ("LIST", "SUMMARY"))
    
    format_enum = Format.LIST if format_input.lower() == Format.LIST.value.lower() else Format.SUMMARY

    button = st.button("Run")

    if query and button:
       output_formatter = OutputFormatter()
       output = ResearchAgentImpl.Run(llm, query, format_enum)
       output = output_formatter._run(output)
       if output:
            st.download_button(label="Download "+format_enum.value+" file",
                            data=output,
                            file_name=query+".txt")
    
    

if __name__ == "__main__":
    main()