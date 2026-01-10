import pytest
from src.log_parser import LogParser, LogEntry

@pytest.fixture
def sample_logs():
    return [
        '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326',
        '192.168.1.5 - - [10/Oct/2000:13:55:36 -0700] "POST /login HTTP/1.0" 404 1024',
        '192.168.1.1 - - [10/Oct/2000:13:55:36 -0700] "GET / HTTP/1.0" NOT_A_NUMBER 100'
    ]

@pytest.mark.parametrize("log_line,expected_ip,expected_status", [
    (
        '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326',
        '127.0.0.1',
        200
    ),
    (
        '192.168.1.5 - - [10/Oct/2000:13:55:36 -0700] "POST /login HTTP/1.0" 404 1024',
        '192.168.1.5',
        404
    ),
    (
        '10.0.0.1 - user123 [15/Dec/2023:08:22:11 +0000] "PUT /api/update HTTP/1.1" 201 512',
        '10.0.0.1',
        201
    ),
    (
        '172.16.254.1 - - [25/Jan/2024:14:30:45 -0500] "DELETE /resource HTTP/2.0" 204 0',
        '172.16.254.1',
        204
    ),
    (
        '8.8.8.8 - admin [01/Jan/2025:00:00:01 +0000] "PATCH /settings HTTP/1.1" 500 2048',
        '8.8.8.8',
        500
    ),
])
def test_parser_logic(log_line, expected_ip, expected_status):
    parser = LogParser()
    result = parser.parse_line(log_line)
    
    assert result.ip_address == expected_ip
    assert result.status_code == expected_status
    assert isinstance(result, LogEntry)

def test_malformed_line():
    parser = LogParser()
    with pytest.raises(ValueError):
        parser.parse_line("This is not a log line")

def test_fixture_integration(sample_logs):
    parser = LogParser()

    valid_logs = sample_logs[:2]
    for log in valid_logs:
        result = parser.parse_line(log)
        assert isinstance(result, LogEntry)
        
    invalid_log = sample_logs[2]
    with pytest.raises(ValueError):
        parser.parse_line(invalid_log)
