from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import ItemList, Item, Summary
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from enum import Enum

class Format(Enum):
    SUMMARY = "Summary"
    LIST = "List"

class ResearchAgentPrompt:
    def __init__(self):

        self.template_str = """  You are a research agent. 
You use duckduckgo_search and Wikipedia (WHICH ARE TOOLS YOU MUST BOTH USE) for different articles and read on the given topic that has been requested for you to research.
Example of calling the duckduckgo_search tool: duckduckgo_search
Example of calling the Wikipedia tool: Wikipedia
When you have finished collecting your findings via duckduckgo_search and Wikipedia (WHICH ARE TOOLS YOU MUST BOTH USE), create an ORIGINAL, IMPERSONAL summarization of your findings IN THE FORMAT SPECIFIED AS THE FINAL ANSWER.
You are not done until you have created an ORIGINAL, IMPERSONAL summary of your findings IN THE FORMAT SPECIFIED AS THE FINAL ANSWER.

{format}
    
Topic: {request}
And remember to create an ORIGINAL, IMPERSONAL summary of the results of this research IN THE FORMAT SPECIFIED AS THE FINAL ANSWER!"""



    def PassInPromptInput(self, request: str, format: Format) -> str:
        format_instructions = self.createFormatInstructions(format)
        
        prompt_template = PromptTemplate(template=self.template_str, input_variables=["request"], partial_variables={"format": format_instructions})
        
        return prompt_template.format(request=request)

    def createFormatInstructions(self, format):
        format_instructions = ''

        if(format == Format.LIST):
            format_instructions = PydanticOutputParser(pydantic_object=ItemList).get_format_instructions()
            itemListExample = self.create_list_example()
            
            example = """
An example of this would be the following:
"""+itemListExample.json()

            format_instructions = format_instructions+example

        else:
            format_instructions = PydanticOutputParser(pydantic_object=Summary).get_format_instructions()
            summaryExample = self.create_summary_example()
            example = """
An example of this would be the following:
"""+summaryExample.json()

            format_instructions = format_instructions+example

        return format_instructions

    def create_list_example(self):
        item1 = Item(item="Chicken Eggs",
            description="Eggs that come from chickens")
        item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
        item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

        itemListExample = ItemList(file_path="eggs.txt",
                        list=[item1, item2, item3])
                    
        return itemListExample

    def create_summary_example(self):
        summary = "Eggs are laid by animals and come from birds, reptiles, fish, amphibians, and even some mamals. They are also consumed in a variey of dishes."

        summaryExample = Summary(file_path="eggs.txt", summary=summary)

        return summaryExample