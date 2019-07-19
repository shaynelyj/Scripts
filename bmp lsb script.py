import binascii

image = open("pico2018-special-logo.bmp","rb").read()
image=image[54:]
#q=0
answer=''
s=''
for c in image:
	print("c: %s"%(c))
	s += chr(ord('0')+(c & 1))
	print("s: %s"%(s))
	if len(s)==8:
		if s == "00000000":
			break
		#print(int(s,2))
		answer+=chr(int(s,2))
		print(answer)
		s=''
		#q+=1
