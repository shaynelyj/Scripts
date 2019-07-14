from pwn import *

context.log_level = 'warn'

iv = 'This is an IV456'.encode('hex')
ct = '5468697320697320616e2049563435360db5d4edcf799c3a6cfc502b10ab1242c1c2808d4b71e31a9ba6fb770194254f1a6579f76b6bb0aa3206023e22f4f8b8ddd7ecf14579dbbfac853ebcc7bf8d11fd8703dce82b480d21dfb56717e3a1ec'

ct = [ct[i:i+32] for i in range(0, len(ct), 32)]

original_block = []
for c in ct:
    original_block.append(c.decode('hex'))

pt = ''
for n_block in range(4,-1,-1):
    zero_byte = 15
    pad_str = ord('\x01')
    inter_state = []
    pad_bytes = ''
    for i in range(16):
        print 'Guessing [{}] bytes...'.format(15-i)
        for j in range(0, 256):
            guess_c2 = ('0'*zero_byte + chr(j) + pad_bytes).encode('hex')
            payload = guess_c2 + ct[-1]

            r = remote('2018shell.picoctf.com',27533)

            r.recvuntil('What is your cookie?\n')
            r.sendline(payload)
            response = r.recv()
            r.close()

            if response.find("invalid padding") == -1:
                temp = chr(pad_str ^ ord(original_block[n_block][zero_byte]) ^ j)
                inter_state.append(temp)

                print 'Found plaintext :', temp.encode('hex')

                pt = temp + pt
                pad_bytes = ''
                for k in range(i+1):
                    pad_bytes += chr((pad_str+1) ^ ord(original_block[n_block][15-k]) ^ ord(inter_state[k]))
                pad_bytes = pad_bytes[::-1]
                break

        pad_str += 1
        zero_byte -= 1
        print 'PLAINTEXT so far', pt.encode('hex')

    print 'Moving to the prev block..'
    del ct[-1]

print 'Decrypted:', pt