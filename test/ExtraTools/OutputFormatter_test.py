from LangChainResearcher.ResearchAgentImpl.ResearchAgentOutputModels import Item, ItemList, Summary
from LangChainResearcher.ExtraTools.OutputFormatter import OutputFormatter

def test_convert_json_to_text_for_list():

    item1 = Item(item="Chicken Eggs",
                 description="Eggs that come from chickens")
    item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
    item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

    itemList = ItemList(list=[item1, item2, item3])

    output_formatter = OutputFormatter()

    itemListString = "1. Chicken Eggs\n2. Duck Eggs\n3. Robin Eggs"

    assert output_formatter.convert_list_to_text(itemList.list) == itemListString

def test_run_can_return_sumary():
    summary = Summary(summary="Eggs are laid by birds, reptiles, fish, amphibians, and even some mammals.")

    output_formatter = OutputFormatter()

    summaryString = "Eggs are laid by birds, reptiles, fish, amphibians, and even some mammals."

    assert output_formatter._run(summary.json()) == summaryString

def test_run_can_handle_an_issue_with_the_object_structure():
        output_formatter = OutputFormatter()
        item1 = Item(item="Chicken Eggs",
                    description="Eggs that come from chickens")
        item2 = Item(item="Duck Eggs", description="Eggs that come from ducks")
        item3 = Item(item="Robin Eggs", description="Eggs that come from robins")

        itemList = ItemList(list=[item1, item2, item3])
        result = output_formatter._run(itemList.json()+"$$")

        assert result.replace(" ", "").replace("\n","") == """The string input has the incorrect format; 
        please correct the format based on the previous format instructions and write to the file. Also, check your input:
    """.replace(" ", "").replace("\n", "")+itemList.json().replace(" ", "").replace("\n", "")+"""$$""".replace(" ", "").replace("\n", "")