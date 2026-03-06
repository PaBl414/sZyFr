import random

def caesar_encrypt(text, key):
    return ''.join(chr((ord(c) + key)) for c in text)

def caesar_decrypt(text, key):
    return ''.join(chr((ord(c) - key)) for c in text)

def key_to_letter(key):
    return chr(64 + key)  # 1=A, 2=B ...

def letter_to_key(letter):
    return ord(letter) - 64

def text_to_binary(text):
    key = random.randint(1, 26)  # żeby mieściło się w literach A-Z
    encrypted = caesar_encrypt(text, key)

    key_letter = key_to_letter(key)
    data = encrypted + key_letter

    binary = ' '.join(format(ord(c), '08b') for c in data)
    return binary

def binary_to_text(binary):
    text = ''.join(chr(int(b, 2)) for b in binary.split())

    encrypted = text[:-1]
    key_letter = text[-1]

    key = letter_to_key(key_letter)

    return caesar_decrypt(encrypted, key)


print("1. Zaszyfrowanie")
print("2. Odszyfrowanie")

choice = input("Wybierz: ")

if choice == "1":
    text = input("Podaj tekst: ")
    print(text_to_binary(text))

elif choice == "2":
    binary = input("Podaj zaszyfrowany: ")
    print(binary_to_text(binary))
else:
    print("Zła opcja")
