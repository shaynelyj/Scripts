from pwn import *

sharecode='owfThf0tytKKT0nXrqJldvFeg9HlJpvdh1gFyek='
cipher=sharecode.decode('base64')
cipher=cipher[:4] + xor(cipher[4], ord('+')^ord('_')) + cipher[5:]
print(cipher.encode('base64'))
