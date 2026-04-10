def shift_letter(letter: int, cifra: int, base: int) -> str:
    code = letter - base;
    code += cifra
    code = code % 26
    code += base
    return chr(code)

def encrypt(message: str, cifra: int) -> str:
    text = []
    for char in message:
        if not char.isalpha():
            text.append(char)
            continue 
        if char.isupper():
            text.append(shift_letter(ord(char), cifra, 65))
            continue
        text.append(shift_letter(ord(char), cifra, 97))
            
    res = "".join(text)
    return res;
    
