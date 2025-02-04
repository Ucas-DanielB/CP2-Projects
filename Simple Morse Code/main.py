# English alphabet and corresponding Morse code
english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', '!', '/', '-', '(', ')', ' ']
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-', '--..--', '..--..', '-.-.--', '-..-.', '-....-', '-.--.', '-.--.-', ' ']

# Function to translate English text to Morse Code
def english_to_morse(english_text):
    # Convert the text to uppercase for consistency
    english_text = english_text.upper()
    
    # Initialize an empty string to store Morse code
    morse_text = ''
    
    # Iterate over each character in the input text
    for char in english_text:
        # Check if the character exists in the alphabet list
        if char in english_alphabet:
            # Find the index of the character and get the corresponding Morse code
            index = english_alphabet.index(char)
            morse_text += morse_code[index] + ' '
        else:
            # Handle invalid characters by adding an error message
            morse_text += '?? '
    
    return morse_text.strip()  # Remove extra space at the end

# Function to translate Morse Code back to English
def morse_to_english(morse_text):
    # Split the Morse code input into individual Morse symbols
    morse_symbols = morse_text.split()
    
    # Initialize an empty string to store English text
    english_text = ''
    
    # Iterate over each Morse symbol in the input
    for symbol in morse_symbols:
        # Check if the symbol exists in the Morse code list
        if symbol in morse_code:
            # Find the index of the symbol and get the corresponding English letter
            index = morse_code.index(symbol)
            english_text += english_alphabet[index]
        else:
            # Handle invalid Morse symbols by adding an error message
            english_text += '?'
    
    return english_text

# Main loop for user interaction
def main():
    while True:
        print("\nChoose an option:")
        print("1. Translate English to Morse Code")
        print("2. Translate Morse Code to English")
        print("3. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Translate English to Morse Code
            english_input = input("Enter the text to translate to Morse Code: ")
            morse_output = english_to_morse(english_input)
            print(f"Morse Code: {morse_output}")
        
        elif choice == '2':
            # Translate Morse Code to English
            morse_input = input("Enter the Morse code to translate to English (separate with spaces): ")
            english_output = morse_to_english(morse_input)
            print(f"English Text: {english_output}")
        
        elif choice == '3':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please choose 1, 2, or 3.")

# Call the main function to start the program
if __name__ == '__main__':
    main()
