from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import ItemList, Item, Summary
from langchain.output_parsers import PydanticOutputParser

class SetPrompts:
    list_output_parser = PydanticOutputParser(pydantic_object=ItemList)

    list_format_instructions = list_output_parser.get_format_instructions()

    item1 = Item(item="Chicken Eggs",
                 description="Eggs that come from chickens")
    item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
    item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

    itemList = ItemList(file_path="output/eggs.txt",
                        list=[item1, item2, item3])

    list_prompt =  """ You are a research agent. 
You browse the web for different articles and read on the given topic that has been requested for you to research.
When you have finished collecting your findings via the search engine, write the content you have collected to a text file via the file write tools.
You are not done until you have written your findings to a text file using the format specified.

Write to the file using the following format:
"""+list_format_instructions+"""
An example of this would be the following:
"""+itemList.json()+"""
Always begin with a '{' and end with a '}'

Research all the different kinds of eggs in the world."""

    summary_output_parser = PydanticOutputParser(pydantic_object=Summary)

    summary_format_instructions = summary_output_parser.get_format_instructions()

    summary_prompt =   """ You are a research agent. 
You browse the web for different articles and read on the given topic that has been requested for you to research.
When you have finished collecting your findings via the search engine, write the content you have collected to a text file via the file write tools.
You are not done until you have written your findings to a text file using the format specified.

Write to the file using the following format:
"""+summary_format_instructions+"""

Research all the different kinds of eggs in the world."""

    request = "Research all the different kinds of eggs in the world."
