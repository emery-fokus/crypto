def chiffrement_cesar (message, key ):
    resultat=""
    for char in message:
        if char.isalpha() :
            base = ord('A') if char.isupper()else ord('a')
            resultat+=chr((ord(char) - base + key) % 26 + base)

        else:
            resultat+=char
    return resultat

message= input("entrer un message :")
key=int(input("entrer un cle :"))
text_chifrre=chiffrement_cesar(message,key)
print(chiffrement_cesar (message, key ))

text_dechiffre=chiffrement_cesar(text_chifrre,-key)
print (f"text_dechiffre:{text_dechiffre}")
    
    











 

   