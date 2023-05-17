from typing import List
from typing import Optional, Type
from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import Item, ItemList
from pydantic import BaseModel
from langchain.tools.file_management.write import WriteFileTool
import json
from json import JSONDecodeError

class FixedWriteFileTool(WriteFileTool):
    description = (
        "Write file to disk." 
        "You must use this tool when you are done with your research"
    )
    args_schema: Optional[Type[BaseModel]] = None

    def convert_list_to_text(self, list: List[Item]):
        formatted_list = ""
        count = 1
        for item in list:
            print(item)
            if count >= 2:
                formatted_list=formatted_list+"\n"
            formatted_list=formatted_list+f"{count}. {item.item}: {item.description}"
            count=count+1
        return formatted_list

        

    def _run(self, itemListString: str) -> str:
        itemList = ItemList.parse_raw(itemListString)
        item_list_string=self.convert_list_to_text(itemList.list)
        return super()._run(itemList.file_path, item_list_string)
