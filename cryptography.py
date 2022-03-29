
#importing the cryptography module
from cryptography.fernet import Fernet

key = Fernet.generate_key()

message = "hello there"

cipher = Fernet(key)
#encrypting the message
encrypted = cipher.encrypt(message)

print(encoded)
#decrypting the message
decrypted = cipher(encoded.decode)