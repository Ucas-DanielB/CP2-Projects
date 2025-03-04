import file_handler
import time_handler

def main():
    file_name = input("Enter the file name: ")

    try:
        content = file_handler.read_file(file_name)
        word_count = file_handler.count_words(content)
        timestamp = time_handler.get_timestamp()

        updated_content = file_handler.append_metadata(content, word_count, timestamp)
        file_handler.write_file(file_name, updated_content)

        print(f"Updated {file_name} with word count: {word_count} and timestamp: {timestamp}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
