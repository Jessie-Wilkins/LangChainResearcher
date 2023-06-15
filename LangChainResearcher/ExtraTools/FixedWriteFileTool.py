from typing import List
from typing import Optional, Type
from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import Item, ItemList, Summary
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from pydantic import BaseModel, ValidationError
from langchain.tools.file_management.write import WriteFileTool
import json
from json import JSONDecodeError

class FixedWriteFileTool(WriteFileTool):
    description = (
        "Write file to disk." 
        "You must use this tool when you are done with your research."
    )
    args_schema: Optional[Type[BaseModel]] = None

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
        

    def _run(self, formattedString: str) -> str:
        formattedString = formattedString.replace("```", "")
        format_error_string = """The string input has the incorrect format; 
    please correct the format based on the previous format instructions and write to the file. Also, check your input:
"""+formattedString
        if(self.check_format(formattedString) == Format.LIST):
            try:
                itemList = ItemList.parse_raw(formattedString)
            except JSONDecodeError:
                return format_error_string
            except ValidationError:
                return format_error_string
            else:
                item_list_string=self.convert_list_to_text(itemList.list)
                return super()._run(itemList.file_path, item_list_string)
        elif(self.check_format(formattedString) == Format.SUMMARY):
            summaryFormat = Summary.parse_raw(formattedString)
            return super()._run(summaryFormat.file_path, summaryFormat.summary)
        else:
            return format_error_string

