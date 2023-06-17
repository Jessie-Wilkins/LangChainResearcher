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
    
    general_prompt_prefix = """  You are a research agent. 
You use duckduckgo_search and Wikipedia (WHICH ARE TOOLS YOU MUST BOTH USE) for different articles and read on the given topic that has been requested for you to research.
Example of calling the duckduckgo_search tool: duckduckgo_search
Example of calling the Wikipedia tool: Wikipedia
When you have finished collecting your findings via duckduckgo_search and Wikipedia (WHICH ARE TOOLS YOU MUST BOTH USE), create an ORIGINAL, IMPERSONAL summarization of your findings IN THE FORMAT SPECIFIED AS THE FINAL ANSWER.
You are not done until you have created an ORIGINAL, IMPERSONAL summary of your findings IN THE FORMAT SPECIFIED AS THE FINAL ANSWER.

"""

    general_prompt_suffix = """

Topic: Research all the different kinds of eggs in the world.
And remember to create an ORIGINAL, IMPERSONAL summary of the results of this research IN THE FORMAT SPECIFIED AS THE FINAL ANSWER!"""

    list_prompt = general_prompt_prefix+list_format_instructions+"""
An example of this would be the following:
"""+itemList.json()+general_prompt_suffix

    summary_output_parser = PydanticOutputParser(pydantic_object=Summary)

    summary_format_instructions = summary_output_parser.get_format_instructions()

    summary_prompt =   general_prompt_prefix+summary_format_instructions+"""
    An example of this would be the following:
    """+summaryExample.json()+general_prompt_suffix

    request = "Research all the different kinds of eggs in the world."
