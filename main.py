# def chiffrement_cesar (message, key ):
#     resultat=""
#     for char in message:
#         if char.isalpha() :
#             base = ord('A') if char.isupper()else ord('a')
#             resultat+=chr((ord(char) - base + key) % 26 + base)

#         else:
#             resultat+=char
#     return resultat

# message= input("entrer un message :")
# key=int(input("entrer un cle :"))
# text_chifrre=chiffrement_cesar(message,key)
# print(chiffrement_cesar (message, key ))

# text_dechiffre=chiffrement_cesar(text_chifrre,-key)
# print (f"text_dechiffre:{text_dechiffre}")


def cesar_cipher(text, key):
	if type(text) == str and type(key) == int:
		return "".join([chr((ord(char) + key) % 1_114_112) for char in text])
	else:
		raise(TypeError)


def cesar_uncipher(crypted_text, key):
		return cesar_cipher(crypted_text, -key)

    

def vigenere_cipher(text,password):
    list_of_keys =[ord(char) for char in password]
    crypted_text=[]
    for index,char in enumerate(text):
        current_key=list_of_keys[index % len(list_of_keys)]
        crypted_text.append(cesar_cipher(char,current_key))
    return"".join(crypted_text)
text=input("entrer un texte:" )
password=input("entrer un mot de passe:")
print(vigenere_cipher(text,password))


    











 

   