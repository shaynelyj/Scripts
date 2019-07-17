'''
If paddingoracle not installed, go to https://github.com/mwielgoszewski/python-paddingoracle 
or git clone https://github.com/mwielgoszewski/python-paddingoracle.git
Go to directory and enter python setup.py install
'''

from pwn import *
from paddingoracle import BadPaddingException, PaddingOracle
import json
from Crypto.Cipher import AES

class PadBuster(PaddingOracle):
    def oracle(self, data):
        while True:
            try:
                r = remote("2018shell.picoctf.com", 27533)
                r.recvuntil("cookie?")
                s = data
                s = str(data).encode("hex")
                r.sendline(s)
                out = r.recvall()
                if "invalid padding" in out:
                    raise BadPaddingException
                return
            except (socket.error, socket.gaierror, socket.herror, socket.timeout) as e:
                print str(e)

if __name__ == '__main__':
    d = {"username": "User", "is_admin": "true", "expires": "2019-10-01"}
    s = json.dumps(d)
    print s
    padbuster = PadBuster()
    encrypted = padbuster.encrypt(s, block_size=AES.block_size, iv="This is an IV456")

    print "Ciphertext: %r" % (str(encrypted).encode("hex"))
