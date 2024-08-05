import requests
print(requests.__version__)
get_payload = {'page': 2, 'count': 25}
r = requests.get("https://httpbin.org/get", params=get_payload)
print(r.status_code)
print(r.ok)
print(r.headers)
print(r.text)
print(r.url)
post_payload = {'username': 'dharani', 'password': 'Python'}
r = requests.post("https://httpbian.org/post", data=post_payload)
print(r.text)
data = r.json()
print(data['form']['password'])
