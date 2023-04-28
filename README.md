# LangChainResearcher
A researcher agent using LangChain that can research any topic I give it and summarize it in a doc.

The purpose of this project is to learn LangChain more and see how far I can push this concept.

## What's needed
Python 3.10
OpenAI key

## Installation
python3 -m env <environment_name> (highly recommend virtual environment)
source <environment_name>/bin/activate (related to above)
pip install -r requirements

### Warning for Mac users
The python package hnwl fails to buid on the Mac.
To bypass this, pass in a flag to the pip command like this:
ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future" pip install -r requirements

## Usage
python main.py

## Documentation
TBD

## Authors
Jessie Wilkins

## License
Just plain old copyright. I'll work on adding one later.
