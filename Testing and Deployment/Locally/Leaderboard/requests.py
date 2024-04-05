import requests

response = requests.get('http://localhost:5000/leaderboard')
print(response.json())
