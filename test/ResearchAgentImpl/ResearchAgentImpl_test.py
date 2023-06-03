import pytest
from LangChainResearcher.ResearchAgentImpl.ResearchAgentPrompt import Format
from LangChainResearcher.ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl
from langchain.llms.fake import FakeListLLM

def test_research_agent_impl_query():
    responses = [
        "Action: FixedWriteFileTool\nAction Input: file.txt, text",
        "Final Answer: File created successfully"
    ]
    fake_llm = FakeListLLM(responses=responses)
    result = ResearchAgentImpl.Run(fake_llm, "Give me an extensive list of dishes from Peru?", Format.LIST)

    assert result == "File created successfully"
