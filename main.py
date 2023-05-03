import sys
import os

from langchain import OpenAI
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ResearchAgentImpl.ResearchAgentImpl import ResearchAgentImpl

def main():
    llm = OpenAI(temperature=0)
    ResearchAgentImpl.Run(llm)

if __name__ == "__main__":
    main()