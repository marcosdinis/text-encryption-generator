def get_upper_letter(letter: int) -> str:
    return

def encrypt(message: str, cifra: int) -> str:
    text = []
    for char in message:
        code = 0;
        if not char.isalpha():
            text.append(char)
            continue 
        if char.isupper():
            text.append(get_upper_letter(char))
            continue;
            
    res = "".join(text)
    return res;
    
