import requests
response = requests.get('https://api.github.com/users/engineersurajsahani')
print(response.json())
