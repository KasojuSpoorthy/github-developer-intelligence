import requests

url = "https://api.github.com/repos/KasojuSpoorthy/github-developer-intelligence/events"

response = requests.get(url)

print(response.status_code)

events = response.json()

print(events)