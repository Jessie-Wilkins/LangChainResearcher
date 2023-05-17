import pytest
import os
from LangChainResearcher.ExtraTools.FixedWriteFileTool import FixedWriteFileTool
from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import Item, ItemList


def test_convert_json_to_text_for_list():

    item1 = Item(item="Chicken Eggs",
                 description="Eggs that come from chickens")
    item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
    item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

    itemList = ItemList(file_path="output/eggs.txt",
                        list=[item1, item2, item3])

    writer = FixedWriteFileTool()

    itemListString = "1. Chicken Eggs: Eggs that come from chickens\n2. Duck Eggs: Eggs that come from ducks\n3. Robin Eggs: Eggs that come from robins"

    assert writer.convert_list_to_text(itemList.list) == itemListString


def test_run_can_create_a_file_in_the_path():
    writer = FixedWriteFileTool()
    item1 = Item(item="Chicken Eggs",
                 description="Eggs that come from chickens")
    item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
    item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

    itemList = ItemList(file_path="output/eggs.txt",
                        list=[item1, item2, item3])
    writer._run(itemList.json())

    assert os.path.isfile(itemList.file_path)   

    with open(itemList.file_path, 'r') as f:
        contents = f.read()
    expected_contents = writer.convert_list_to_text(itemList.list)
    assert contents == expected_contents

    os.remove(itemList.file_path)

