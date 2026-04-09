def decode_mars_message():
    print("--- Mars Message Decoder ---")
    
    encoded = input("Enter the encrypted message: ").strip().upper()   #getting the secret message from the user
                                                                       #.upper() converts to uppercase
    decoded_result = ""
    
    # We loop through the message using 'enumerate' to get the position (i)
    # The shift for the first letter is 1, second is 2, and so on [cite: 92-94]
    for i, char in enumerate(encoded):
        if char.isalpha():
            # Calculate the shift (index + 1)
            shift = i + 1
            
            # Convert letter to a number (0-25), subtract shift, and wrap around
            # ord('A') is 65, so subtracting it turns 'A' into 0
            original_pos = (ord(char) - ord('A') - shift) % 26
            
            # Convert number back to a letter
            decoded_char = chr(original_pos + ord('A'))
            decoded_result += decoded_char
        else:
            # If there's a space or number, just keep it as is
            decoded_result += char
             
    print(f"Decoded Output: {decoded_result}")              #the final output should always be in all caps

if __name__ == "__main__":
    decode_mars_message()