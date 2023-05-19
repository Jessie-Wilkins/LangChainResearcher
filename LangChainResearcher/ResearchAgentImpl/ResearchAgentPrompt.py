from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import ItemList, Item, Summary
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from enum import Enum

class Format(Enum):
    SUMMARY = "Summary"
    LIST = "List"

class ResearchAgentPrompt:
    def __init__(self):

        self.template_str = """ You are a research agent. 
You browse the web and wikipedia for different articles and read on the given topic that has been requested for you to research.
When you have finished collecting your findings via the search engine and wikipedia, write the content you have collected to a text file via the file write tools.
You are not done until you have written your findings to a text file using the format specified.

Write the output to the file using the following format:
{format}
    
Topic: {request}
And remember to write the results of this research to a file!"""



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

        return format_instructions

    def create_list_example(self):
        item1 = Item(item="Chicken Eggs",
            description="Eggs that come from chickens")
        item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
        item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

        itemListExample = ItemList(file_path="output/eggs.txt",
                        list=[item1, item2, item3])
                    
        return itemListExample