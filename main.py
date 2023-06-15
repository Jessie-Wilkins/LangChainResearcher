from langchain.chat_models import ChatOpenAI
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl
import streamlit as st

def main():
    llm = ChatOpenAI(temperature=0)
    query = st.text_input("What is the topic you want to research?")
    format_input = st.selectbox("Do you want this in a LIST or a SUMMARY format?", ("LIST", "SUMMARY"))
    while (format_input.lower() != Format.LIST.value.lower() and format_input.lower() != Format.SUMMARY.value.lower()):
        format_input = input("Input was incorrect. You must type either LIST or SUMMARY for your answer. Which format do you want: ")
    
    format_enum = Format.LIST if format_input.lower() == Format.LIST.value.lower() else Format.SUMMARY

    button = st.button("Run")

    if query and button:
       output = st.write(ResearchAgentImpl.Run(llm, query, format_enum))
       if output:
        with open(query+".txt", "rb") as file:
            st.download_button(label="Download "+format_enum+" file",
                            data=file,
                            file_name=query+".txt")
    
    

if __name__ == "__main__":
    main()