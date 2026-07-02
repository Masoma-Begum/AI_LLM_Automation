import pytest
from prompts.prompt_builder import get_prompt
from llm_clients.openai_client import get_llm_response
from evaluation.response_validator import validate_response

def test_api_prompt():
   prompt = get_prompt("API testing")
   response = get_llm_response(prompt)
   assert validate_response(response)
