ALPHABET= "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯабвгдеёжзийклмнопрстуф\
хцчшщыэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def ceasar_cipher(text=str, shift=int):
    result =[]
    for symbol in text:
        if symbol in ALPHABET:
            old_index = ALPHABET.index(symbol)
            new_index = (old_index + shift) % len(ALPHABET)
            result.append(ALPHABET[new_index])
        else:
            result.append(symbol)
    return "".join(result)

def encode(text, shift):
    return ceasar_cipher(text, shift)

def decode(text, shift):
    return ceasar_cipher(text, -shift)

example1 = "Hola, AMIGO, ПРИВЕТ амиго!!"
example2 = "Jqnc, COKIQ, СТКДЗФ вокер!!"

print(encode(example1, 2))
print(decode(example2, 2))

print(encode("I'm not afraid to be out of range", 12300))
print(decode("х'V WXc JOaJRM cX KN Xdc XO aJWPN", 12300))