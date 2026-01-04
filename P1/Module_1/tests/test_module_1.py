import pytest
from src.process_stream import process_stream

def test_process_stream():

    results = list(process_stream(limit=16))
    
    # Assert: Verify length
    assert len(results) == 15, "Stream should produce 15 items for limit=16"
    
    assert results[2] == "Data", "3 should yield 'Data'"
    assert results[4] == "Engineering", "5 should yield 'Engineering'"
    assert results[14] == "DataEngineering", "15 should yield 'DataEngineering'"

    assert results[0] == "1", "1 should yield '1'"