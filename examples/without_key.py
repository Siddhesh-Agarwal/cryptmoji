from cryptmoji import Cryptmoji

if __name__ == "__main__":
    text = "Hello World!"
    a = Cryptmoji(text)
    encrypted = a.encrypt()
    print(encrypted)
    decrypted = a.decrypt()
    print(decrypted)
