from cryptmoji import encrypt, decrypt

if __name__ == "__main__":
    text = "Hello World!"
    encrypted = encrypt(text)
    print(f"{encrypted=}")
    decrypted = decrypt(encrypted)
    print(f"{decrypted=}")
    assert decrypted == text
