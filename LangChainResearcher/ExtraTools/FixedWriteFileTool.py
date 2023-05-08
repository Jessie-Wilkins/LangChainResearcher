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
        "Takes the file path and the text content as two string arguments."
        "An example of this input: \"file_path\": \"test.txt\", \"text\": \"This is some test text.\""
        "Follow this example strictly; make sure to always use the double quotes just like in the example when working with the real inputs."
        "If a user asks for a specific format, change the text value to follow that format."
    )
    args_schema: Optional[Type[BaseModel]] = None

    @staticmethod
    def is_valid_json(input_string):
        try:
            json.loads(input_string)
            return True
        except JSONDecodeError:
            return False

    def convert_list_to_text(file_path: str, list: List[Item]):
        return ""

        

    def _run(self, file_path_and_text: str) -> str:
        print()
        print(file_path_and_text)
        file_path_and_text = "{\"" + file_path_and_text + "\"}"
        print()
        print(file_path_and_text)
        file_path_and_text_json = None
        if FixedWriteFileTool.is_valid_json(file_path_and_text):
            file_path_and_text_json = json.loads(file_path_and_text)
            return super()._run(file_path_and_text_json["file_path"], file_path_and_text_json["text"])
        else:
            return "Failed to write file."