from cryptmoji import Cryptmoji

if __name__ == "__main__":
    text = "Hello World!"
    key = "random_key"
    a = Cryptmoji(text, key)
    encrypted = a.encrypt()
    print(encrypted)
    decrypted = a.decrypt()
    print(decrypted)
