import requests
with open("usernames.txt", 'r') as f:
	usernames=[line.strip() for line in f]
with open("passwords.txt", 'r') as f:
	passwords=[line.strip() for line in f]
payload = dict(zip(usernames,passwords))
for username, password in payload.items():
	r = requests.get('https://httpbin.org/basic-auth/lol/lol', auth=(username,password));
	if not r.ok:
		continue
	
	else:
		print(r.text)
	

