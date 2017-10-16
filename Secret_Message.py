def find_message(text):
    secret_message = ""
    for character in text:
        if (character.isupper()==True):
            secret_message+=character
    return secret_message


find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
 