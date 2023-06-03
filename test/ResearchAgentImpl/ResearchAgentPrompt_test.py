import pytest
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import ResearchAgentPrompt, Format
from test.ResearchAgentImpl.set_prompts import SetPrompts


@pytest.fixture(scope='module')
def setup_agent_prompt():
    agent_prompt = ResearchAgentPrompt()
    # setup code
    yield agent_prompt

def test_that_prompt_is_formatted_as_list(setup_agent_prompt):
    prompt = setup_agent_prompt.PassInPromptInput(request=SetPrompts.request, format=Format.LIST)
    assert prompt.replace(" ", "") == SetPrompts.list_prompt.replace(" ", "")

def test_that_prompt_is_formatted_as_summary(setup_agent_prompt):
    prompt = setup_agent_prompt.PassInPromptInput(request=SetPrompts.request, format=Format.SUMMARY)
    assert prompt.replace(" ", "") == SetPrompts.summary_prompt.replace(" ", "")