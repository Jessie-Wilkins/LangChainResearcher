# LangChainResearcher
A researcher agent using LangChain that can research any topic I give it and summarize it in a doc.

The purpose of this project is to learn LangChain more and see how far I can push this concept.

## What's needed
Python 3.10
OpenAI key (see [here](https://platform.openai.com/docs/guides/production-best-practices/api-keys) on how to get one)

## Installation
python3 -m env <environment_name> (highly recommend virtual environment)
source <environment_name>/bin/activate (related to above)
pip install -r requirements

### Warning for Mac users
The python package hnwl fails to buid on the Mac.
To bypass this, pass in a flag to the pip command like this:
ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future" pip install -r requirements

## Usage
```python main.py```

### General Warning
The LLM sometimes gives inconsistent results and even can produce errors. If this happens, run it again

## Testing
```pytest```

## Authors
Jessie Wilkins

## License
Just plain old copyright. I'll work on adding one later.
