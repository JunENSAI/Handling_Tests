from dataclasses import dataclass
import re

@dataclass
class LogEntry:
    ip_address: str
    timestamp: str
    status_code: int

class LogParser:
    def __init__(self):

        self.pattern = re.compile(
            r'^(?P<ip>[\d.]+)\s+'
            r'.*?' 
            r'\[(?P<timestamp>[^\]]+)\]\s+' 
            r'"[^"]*"\s+'
            r'(?P<status>\d+)'
        )
    
    def parse_line(self, line: str) -> LogEntry:
        """
        Parse a log line and extract IP address, timestamp, and status code.
        
        Args:
            line: A string containing a log entry
            
        Returns:
            LogEntry object if parsing succeeds, None otherwise
        """
        match = self.pattern.match(line)
        
        if match:
            return LogEntry(
                ip_address=match.group('ip'),
                timestamp=match.group('timestamp'),
                status_code=int(match.group('status'))
            )
        
        raise ValueError(f"Invalid log format: {line}")