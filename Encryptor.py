def text_to_binary(text):
    words = text.split()
    binary_words = []
    
    for word in words:
        binary_letters = []
        for char in word:
            if char.isalpha():
                if char.islower():
                    pos = ord(char) - ord('a') + 1  # Lowercase 1–26
                else:
                    pos = ord(char) - ord('A') + 27  # Uppercase 27–52
                binary_letters.append(bin(pos)[2:])
        
        binary_words.append(" ".join(binary_letters))
    
    return "  ".join(binary_words)

information = input("Enter text: ")
print("Binary: ", text_to_binary(information))
print(" ")
input("Press "Space" or "Enter" to close.")
