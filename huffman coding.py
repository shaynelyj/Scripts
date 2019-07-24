from PIL import Image
bmp = Image.open("red0.bmp")
rgb_bmp = bmp.convert("RGB")
for i in range(0, 256):
    r, g, b = rgb_bmp.getpixel((i, 0))
    #print(r & 1,end="")

q="0000010100101101000010011010001010100011010101001100101000101100110001110111111001100111011111000000111100010010110011001111101010001100011111011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"

dict={
	"000":"s",
	"0010":"u",
	"0011":"_",
	"010":"0",
	"0110":'d',
	"0111":"9",
	"1000":"5",
	"10010":"n",
	"10011":"h",
	"10100":"1",
	"10101":"a",
	"10110":"e",
	"10111":"b",
	"1100":"1",
	"11010":"{",
	"11011":"}",
	"11100":"r",
	"11101":"c",
	"11110":"k",
	"11111":"3"
}

ans=""
z=0
while q:
	for _ in range(3,6):
		if q[:_] in dict:
			ans+=dict[q[:_]]
			print(ans)
			q=q[_:]
