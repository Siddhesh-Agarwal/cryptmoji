from cryptmoji import encrypt, decrypt

if __name__ == "__main__":
    text = "Hello World!"
    key = "random_key"
    encrypted = encrypt(text, key=key)
    print(f"{encrypted=}")
    decrypted = decrypt(encrypted, key=key)
    print(f"{decrypted=}")
    assert decrypted == text
