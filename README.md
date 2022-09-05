# Cryptmoji

A simple emoji-based encryption-decryption library.
_______________________

## Installation

pip install the library:

```sh
pip install cryptmoji
```

## Usage

```python
from cryptmoji import Cryptmoji

text = "Hello World!"
key = "random_key" # makes the encryption stronger (optional)
a = Cryptmoji(text, key=key)
encrypted = a.encrypt()
print(encrypted)
decrypted = a.decrypt()
print(decrypted)
```
