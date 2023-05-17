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

    itemListString = "1. Chicken Eggs\n2. Duck Eggs\n3. Robin Eggs"

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

def test_run_can_handle_an_issue_with_the_object_structure():
    writer = FixedWriteFileTool()
    item1 = Item(item="Chicken Eggs",
                 description="Eggs that come from chickens")
    item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
    item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

    itemList = ItemList(file_path="output/eggs.txt",
                        list=[item1, item2, item3])
    result = writer._run(itemList.json()+"$$")

    assert result.replace(" ", "").replace("\n","") == """The string input has the incorrect format; 
    please correct the format based on the previous format instructions and write to the file.
""".replace(" ", "").replace("\n", "")

