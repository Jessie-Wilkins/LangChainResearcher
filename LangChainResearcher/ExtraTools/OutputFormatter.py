from typing import Optional, Type, List
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools.base import BaseTool
from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import Item, ItemList, Summary
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from json import JSONDecodeError
from pydantic import ValidationError

class OutputFormatter(BaseTool):
    name = "output_formatter"
    description = ("A tool that returns a formatted string."
                   "Useful for returning an output in a particular printable format as the final answer."
                   "Input should be the formatted content specified by the user.")
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""

        format_error_string = """The string input has the incorrect format; 
    please correct the format based on the previous format instructions and write to the file. Also, check your input:
"""+query
        if(self.check_format(query) == Format.LIST):
            try:
                itemList = ItemList.parse_raw(query)
            except JSONDecodeError:
                return format_error_string
            except ValidationError:
                return format_error_string
            else:
                item_list_string=self.convert_list_to_text(itemList.list)
                return item_list_string
        elif(self.check_format(query) == Format.SUMMARY):
            summaryFormat = Summary.parse_raw(query)
            return summaryFormat.summary
        else:
            return format_error_string
        
    async def _arun(self, query: str,  run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("OutputFormatter does not support async")
    
    def convert_list_to_text(self, list: List[Item]):
        formatted_list = ""
        count = 1
        for item in list:
            print(item)
            if count >= 2:
                formatted_list=formatted_list+"\n"
            formatted_list=formatted_list+f"{count}. {item.item}"
            count=count+1
        return formatted_list
    
    def check_format(self, formatted_string) -> Format:
        try:
            ItemList.parse_raw(formatted_string)
            return Format.LIST
        except JSONDecodeError:
            print("\nNot List")
        except ValidationError:
            print("\nNot List")
        
        try:
            Summary.parse_raw(formatted_string)
            return Format.SUMMARY
        except JSONDecodeError:
            print("\nNot Summary")
        except ValidationError:
            print("\nNot Summary")