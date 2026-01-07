import pytest

# Fixture 1: The Raw Data
@pytest.fixture
def raw_logs():
    return [
        "2025-01-01 10:00:00 - INFO - System started",
        "2025-01-01 10:01:05 - ERROR - Connection failed",
        "2025-01-01 10:02:00 - INFO - User logged in"
    ]

# Fixture 2: The Logic (Dependency Injection)
@pytest.fixture
def parsed_logs(raw_logs):
    parsed_data = []
    for line in raw_logs:
        # Split by " - " to separate the 3 parts cleanly
        parts = line.split(" - ")
        
        # Create a structured dictionary
        entry = {
            "timestamp": parts[0],
            "level": parts[1],
            "message": parts[2]
        }
        parsed_data.append(entry)
    
    return parsed_data

# Test A: Using the Raw Data directly
def test_raw_count(raw_logs):
    assert len(raw_logs) == 3

# Test B: Using the Processed Data
def test_parsed_error(parsed_logs):
    errors = [x for x in parsed_logs if x['level'] == "ERROR"]
    
    assert len(errors) == 1
    assert errors[0]['message'] == "Connection failed"