import requests

url = "https://dog.ceo/api/breeds/image/random"

response = requests.request("GET", url)

print(response.text)