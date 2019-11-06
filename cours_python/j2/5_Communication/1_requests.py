# apt-get install python3-requests
# ou: pip3 install requests
# http://docs.python-requests.org/en/master/user/quickstart/

import requests

r = requests.get('https://api.github.com/events')

r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# Multiple payload
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# Cookies
url = 'https://httpbin.org/cookies'
cookies = dict(join_the_dark_side='we have cookies!')
r = requests.get(url, cookies=cookies)
print(r.text)

# History des redirection
url = 'http://facebook.com'
r = requests.get(url)
r.history
fd = open('/tmp/facebook.html', 'w')
fd.write(r.text)    # ouvrir /tmp/facebook.html (attention fishing !)

r = requests.get('https://api.github.com/events')
print(r.text)

