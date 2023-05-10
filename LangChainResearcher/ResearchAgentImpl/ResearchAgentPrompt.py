from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import ItemList, Summary
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from enum import Enum

class Format(Enum):
    SUMMARY = "Summary"
    LIST = "List"

class ResearchAgentPrompt:
    def __init__(self):
        self.template_str = """ You are a research agent. 
You browse the web for different articles and read on the given topic that's request to research.
When you have finished collecting your findings, write the content you have collected to a text file.
You are not done until you have written your findings to a text file using the format specified.

Write to the file using the following format:
{format}
    
{request}"""


    def PassInPromptInput(self, request: str, format: Format) -> str:
        format_instructions = self.createFormatInstructions(format)
        
        prompt_template = PromptTemplate(template=self.template_str, input_variables=["request"], partial_variables={"format": format_instructions})
        
        return prompt_template.format(request=request)

    def createFormatInstructions(self, format):
        format_instructions = ''

        if(format == Format.LIST):
            format_instructions = PydanticOutputParser(pydantic_object=ItemList).get_format_instructions()

        else:
            format_instructions = PydanticOutputParser(pydantic_object=Summary).get_format_instructions()

        return format_instructions