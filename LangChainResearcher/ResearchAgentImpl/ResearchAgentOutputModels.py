from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    item: str = Field(description="the particular name, item, or entity produced from the research.")
    # description: str = Field(description="a description of the name, item, or entity that is several sentences long.")

class ItemList(BaseModel):
    list: List[Item] = Field(description="A list of items and their descriptions.")
        
class Summary(BaseModel):
    summary: str = Field(description="Several sentences describing the results of the research.")