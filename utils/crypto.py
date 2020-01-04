from Crypto import Random
from Crypto.Cipher import AES

import base64
import hashlib


class Cripto(object):

    def __init__(self):
        self.bs = 32
        self.base_key = "b04231f7737d4b059c15f5ac41aa7366"
        self.key = hashlib.sha256(self.base_key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(str(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(str(enc))
        iv = enc[: AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size :])).decode("utf-8")

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[: -ord(s[len(s) - 1 :])]
