 
#Encrypts a message using a keyword cipher.

def keyword_cipher(key, message):
    cipher_alphabet = []
    seen = set()
    
    
    for char in key.upper():
        if char.isalpha() and char not in seen:
            cipher_alphabet.append(char)
            seen.add(char)
    
    
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            cipher_alphabet.append(char)
    
    
    plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    encrypted = []
    for char in message:
        if char.isalpha():
           
            is_upper = char.isupper()
            char_upper = char.upper()
            
       
            pos = plain_alphabet.index(char_upper)
            cipher_char = cipher_alphabet[pos]
            
            
            encrypted.append(cipher_char if is_upper else cipher_char.lower())
        else:
            
            encrypted.append(char)
    
    return "".join(encrypted)



print(keyword_cipher("mubashir", "edabit"))  
