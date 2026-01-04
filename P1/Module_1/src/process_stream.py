from typing import Generator

def process_stream(limit: int) -> Generator[str, None, None]:
    
    for i in range(1, limit):
        if i % 15 == 0:
            yield "DataEngineering"
        elif i % 3 == 0:
            yield "Data"
        elif i % 5 == 0:
            yield "Engineering"
        else:
            yield str(i)