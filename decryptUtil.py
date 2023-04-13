import argparse
import base64
import array
import hashlib

from Cryptodome.Cipher import AES


def aes_cbc_decrypt(decodedPass, key, iv):
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    crypter = AES.newÍ(key, AES.MODE_CBC, iv)
    decryptedPassword = unpad(crypter.decrypt(decodedPass))
    return decryptedPassword.decode('utf-8')

def decrypt(encryptedPass, secret):
    decodedPass = base64.b64decode(encryptedPass)
    iv = decodedPass[:16]
    decodedPass = decodedPass[16:]

    salt = array.array('b', [6, -74, 97, 35, 61, 104, 50, -72])
    key = hashlib.pbkdf2_hmac("sha256", secret.encode(), salt, 5000, 32)

    
    try:
        decrypted = aes_cbc_decrypt(decodedPass, key, iv)
        if (decrypted == ''):
            raise Exception('\nMaybe the password is incorrect.')

    except Exception as e:
        print('\nError during decryption. This script is tested only for SQL Developer 18+. ---- '+ str(e) )
    
    return decrypted
