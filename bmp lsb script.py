import binascii

image = open("pico2018-special-logo.bmp","rb").read()
image=image[54:]
s=""
a=""
for c in image:
	s+=str(c)
	if len(s)==8:
		if s == "00000000":
			break
		a+=(chr(int(s,2)))
		print(a)
		s=""
