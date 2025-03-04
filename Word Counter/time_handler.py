from datetime import datetime

def get_timestamp():
    """Returns a formatted timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
