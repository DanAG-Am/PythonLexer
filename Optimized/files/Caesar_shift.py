cyphertext = ""
key = 0
plaintext = ""
letters = "abcdefghijklmnopqrstuvwxyz"

def decrypt() : 
    cyphertext = input("Ingresa el cifrado a decodificar:       >>> ")
    plaintext = ""
    key = int(input("Key?       >>> "))
    for ch in cyphertext:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - key) % 26
            new_char = letters[new_pos]
            plaintext += new_char
            print(new_char)
        else:
            plaintext += ch
    print("El decriptado es:\n")

decrypt()