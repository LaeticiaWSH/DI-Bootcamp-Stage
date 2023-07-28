import requests 

response = requests.get("https://www.vatel.mu")
print(response.elapsed)
