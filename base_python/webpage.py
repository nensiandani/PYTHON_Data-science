import requests as req

url = 'https://www.facebook.com/favicon.ico'
file = req.get(url,allow_redirects=True)
open('facebook.ico','wb').write(file.content)
