from .encryption_interface import IEncryptor

class XOrEncryption(IEncryptor):
    def encrypt(self, data):
        key = "interpreter"
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))


    def decrypt(self, data):
        key = "interpreter"
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

        