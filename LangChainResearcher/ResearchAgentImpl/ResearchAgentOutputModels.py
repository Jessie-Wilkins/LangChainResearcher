from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    item: str = Field(description="the particular name, item, or entity produced from the research.")
    # description: str = Field(description="a description of the name, item, or entity that is several sentences long.")

class ItemList(BaseModel):
    file_path: str = Field(description="the file path that the content will be written to.")
    list: List[Item] = Field(description="A list of items and their descriptions.")
        
class Summary(BaseModel):
    file_path: str = Field(description="the file path that the content will be written to.")
    summary: str = Field(description="This is a several paragraph essay describing the results of the research.")