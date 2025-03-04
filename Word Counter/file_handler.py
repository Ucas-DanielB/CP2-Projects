def read_file(file_name):
    """Reads content from a file."""
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(content):
    """Counts words in the given text."""
    return len(content.split())

def append_metadata(content, word_count, timestamp):
    """Appends or updates word count and timestamp in the content."""
    lines = content.strip().split("\n")
    
    if lines and lines[-1].startswith("Word Count:"):
        lines = lines[:-2]  # Remove previous word count and timestamp
    
    lines.append(f"Word Count: {word_count}")
    lines.append(f"Last Updated: {timestamp}")

    return "\n".join(lines)

def write_file(file_name, content):
    """Writes updated content back to the file."""
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
