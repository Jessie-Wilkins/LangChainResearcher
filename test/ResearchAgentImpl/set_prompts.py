from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import ItemList, Item, Summary
from langchain.output_parsers import PydanticOutputParser

class SetPrompts:
    list_output_parser = PydanticOutputParser(pydantic_object=ItemList)

    list_format_instructions = list_output_parser.get_format_instructions()

    item1 = Item(item="Chicken Eggs",
                 description="Eggs that come from chickens")
    item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
    item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

    itemList = ItemList(file_path="eggs.txt",
                        list=[item1, item2, item3])
    summary = "Eggs are laid by animals and come from birds, reptiles, fish, amphibians, and even some mamals. They are also consumed in a variey of dishes."

    summaryExample = Summary(file_path="eggs.txt", summary=summary)
    
    general_prompt_prefix = """ You are a research agent. 
You browse the web and wikipedia for different articles and read on the given topic that has been requested for you to research.
When you have finished collecting your findings via the search engine and wikipedia, delete all files that exist via the delete tool (except the file you are currently writing to) and write the content you have collected to a text file (the name should be the same as the query) via the file write tools.
You are not done until you have delete all existing files (except the file you are currently writing to) and written your findings to a text file (the name should be the same as the query) using the format specified.

Write the output to the file using the following format:
"""

    general_prompt_suffix = """

Topic: Research all the different kinds of eggs in the world.
And remember delete all currently existing files (except the file you are currently writing to) and to write the results of this research to a file (the name should be the same as the query)!"""

    list_prompt = general_prompt_prefix+list_format_instructions+"""
An example of this would be the following:
"""+itemList.json()+general_prompt_suffix

    summary_output_parser = PydanticOutputParser(pydantic_object=Summary)

    summary_format_instructions = summary_output_parser.get_format_instructions()

    summary_prompt =   general_prompt_prefix+summary_format_instructions+"""
    An example of this would be the following:
    """+summaryExample.json()+general_prompt_suffix

    request = "Research all the different kinds of eggs in the world."
