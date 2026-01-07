from datetime import datetime

def standardize_date(date_str: str) -> str:
    """
    Parses various date string formats and converts them to ISO 8601.
    
    Supported formats:
    - MM/DD/YYYY (e.g., "12/01/2023")
    - YYYY.MM.DD (e.g., "2023.12.01")
    
    Args:
        date_str (str): The raw date string.
        
    Returns:
        str: The date in "YYYY-MM-DD" format.
        
    Raises:
        ValueError: If the format is not recognized.
    """
    fmt_options = [
        "%m/%d/%Y",  # 12/01/2023
        "%Y.%m.%d",  # 2023.12.01
    ]
    
    for fmt in fmt_options:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
            
    # If no format matched
    raise ValueError(f"Date format not recognized: {date_str}")