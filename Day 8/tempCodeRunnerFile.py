def convert_cipher(text,shift):
    cipher_text = "".join(
        chr(ord(char)+shift) if char.isalnum() else char for char in text
    )


def decode_cipher(text,shift):
    decoded_text = "".join(
        chr(ord(char)-shift) if char.isalnum() else char for char in text
    )