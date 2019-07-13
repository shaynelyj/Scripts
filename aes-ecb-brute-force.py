#Amend "p=remote"
#When executing, run "python aes-ecb-brute-force.py | grep Flag"

from pwn import *
q='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_{@}$!"#%&()*+,-./:;<=>?[]^`|~'
k=""
for z in range(48):
	for _ in q:
		p=remote("2018shell.picoctf.com",30399)
		prompt=p.readuntil('situation report: ')
		p.sendline("x"*(59-len(k))+"fying code is: "+k+_+"Y"*(48-len(k)))
		e=p.read(4096)
		if e[224:256]==e[384:416]:
			k+=_
			print("Flag: %s" %(k))
			break
