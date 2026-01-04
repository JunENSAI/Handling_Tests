import pytest
from src.json_tools import flatten_json

@pytest.mark.unit
def test_happy_path():

    input_data = flatten_json({"user": {"name": "Alice", "address": {"city": "Paris"}}})
    
    result = {"user_name": "Alice", "user_address_city": "Paris"}

    assert result == input_data

@pytest.mark.unit
def test_empy_case():

    input_data = flatten_json({})

    assert input_data == {}

@pytest.mark.unit
def test_ambiguity_case():

    input_data = flatten_json({"groups": ["admin", "editor"]})

    assert input_data == {"groups": ["admin", "editor"]}