def binary_to_text(bin_str):
    words_bin = bin_str.split("  ")
    decoded_words = []
    
    for word in words_bin:
        letters_bin = word.split()
        word_decoded = ""
        
        for b in letters_bin:
            pos = int(b, 2)
            if 1 <= pos <= 26:
                buchstabe = chr(pos - 1 + ord('a'))  # Kleinbuchstaben
            else:
                buchstabe = chr(pos - 27 + ord('A'))  # Großbuchstaben
                
            word_decoded += buchstabe
        
        decoded_words.append(word_decoded)
    
    return " ".join(decoded_words)

information = input("Gib den Binärcode ein: ")
print("In Latin Letters:", binary_to_text(information))
print(" ")
input("Press "Space" or "Enter" to close.")
