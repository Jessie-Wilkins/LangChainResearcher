from langchain.prompts import PromptTemplate
from enum import Enum

class Format(Enum):
    SUMMARY = "Summary"
    LIST = "List"

class ResearchAgentPrompt:

    template_str = """ You are a research agent. You browse the web for different articles and read on the given topic that's request to research.
    When you are asked for a list format, write it in the following format:

    1. Item1\n
    2. Item2\n
    3. Item3\n

    When you are asked for a summary format, write it in the following format:
    This is the first sentence of a summary. This is the second sentence of the summary. This is the third sentence. 
    This is the fourth sentence. This is the fifth sentence.

    This is the sixth sentence in a new paragraph.


    For the above format, separate into paragraphs of five sentences or fewer. 
    You should not start writing a new paragraph until the current paragraph is at five sentences.

    {request}

    Write in the {format} format."""

    def __init__(self):
        self.prompt_template = PromptTemplate(template=self.template_str, input_variables=["request", "format"])

    def PassInPromptInput(self, request: str, format: Format) -> str:
        return self.prompt_template.format(request=request, format=format.value)