# Standard Morse Code Dictionary 
MORSE_DICT = {                                                         #mapping each alphabet to its morse code
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0', '/': ' ' 
}

def decode_morse(message):
    #Split the message into words (separated by ' / ' or '   ')
    #and letters (separated by a single space)
    words = message.split(' / ')
    decoded_message = []

    for word in words:
        chars = word.split()     #split each word into individual morse characters
        decoded_word = "".join(MORSE_DICT.get(c, '?') for c in chars) #look up each character and join them
        decoded_message.append(decoded_word)

    return " ".join(decoded_message)

def main():
    print("--- Mars Rover Morse Code Decipher ---")
    print("Instructions: Enter Morse code using '.' and '-'.")
    print("Separate letters with a space and words with ' / '.")
    
    user_input = input("\nEnter Morse Code: ").strip()
    
    if user_input:
        decoded_text = decode_morse(user_input)
        print(f"\nDecoded Message: {decoded_text}")
    else:
        print("No input detected.")

if __name__ == "__main__":
    main()