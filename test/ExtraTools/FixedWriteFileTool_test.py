import pytest
from LangChainResearcher.ExtraTools.FixedWriteFileTool import FixedWriteFileTool
from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import Item, ItemList

def test_convert_json_to_text_for_list():

        item1 = Item(item="Chicken Eggs", description="Eggs that come from chickens")
        item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
        item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

        itemList = ItemList(file_path="output/eggs.txt", list=[item1, item2, item3])

        writer = FixedWriteFileTool()

        itemListString = """1. Chicken Eggs: Eggs that come from chickens\n
        2. Duck Eggs: Eggs that come from ducks\n
        3. Robin Eggs: Eggs that come from robins"""

        assert writer.convert_list_to_text(itemList) == itemListString