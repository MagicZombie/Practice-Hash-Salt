from hashlib import sha256, pbkdf2_hmac
from bcrypt import gensalt
from binascii import hexlify

password = input("Enter Password: ")
password = password.encode()
salt = gensalt()

hash_pw = pbkdf2_hmac('sha256', password, salt, 100000)
saved_hash = hexlify(hash_pw)
saved_hash = saved_hash.decode('UTF-8')
saved_salt = salt.decode('UTF-8')
print(saved_hash)
print(saved_salt)

input("Press any key to exit.")
