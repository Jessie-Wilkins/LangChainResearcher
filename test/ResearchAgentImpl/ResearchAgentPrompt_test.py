from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import ResearchAgentPrompt, Format
import pytest

formatted_prompt = """ You are a research agent. You browse the web for different articles and read on the given topic that's request to research.
    When you are asked for a list format, write it in the following format:
    1. Item1
    2. Item2
    3. Item3

    When you are asked for a summary format, write it in the following format:
    This is the first sentence of a summary. This is the second sentence of the summary. This is the third sentence. 
    This is the fourth sentence. This is the fifth sentence.

    This is the sixth sentence in a new paragraph.


    For the above format, separate into paragraphs of five sentences or fewer. 
    You should not start writing a new paragraph until the current paragraph is at five sentences.

    Research all the different kinds of eggs in the world.

    Write in the List format."""

def test_that_prompt_is_formatted():
    request = "Research all the different kinds of eggs in the world."
    
    agent_prompt = ResearchAgentPrompt()

    prompt = agent_prompt.PassInPromptInput(request=request, format=Format.LIST)

    assert prompt == formatted_prompt