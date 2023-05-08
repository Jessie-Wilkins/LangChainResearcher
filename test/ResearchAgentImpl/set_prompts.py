from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import ItemList, Summary
from langchain.output_parsers import PydanticOutputParser

class SetPrompts:
    list_output_parser = PydanticOutputParser(pydantic_object=ItemList)

    list_format_instructions = list_output_parser.get_format_instructions()

    list_prompt =  """ You are a research agent. 
You browse the web for different articles and read on the given topic that's request to research.

"""+list_format_instructions+"""

Research all the different kinds of eggs in the world."""

    summary_output_parser = PydanticOutputParser(pydantic_object=Summary)

    summary_format_instructions = summary_output_parser.get_format_instructions()

    summary_prompt =   """ You are a research agent. 
You browse the web for different articles and read on the given topic that's request to research.

"""+summary_format_instructions+"""

Research all the different kinds of eggs in the world."""

    request = "Research all the different kinds of eggs in the world."
