import requests

link = "http://localhost:5000/frases_motivacionais"

req = requests.get(link)

filtra_req = req.json()

print(filtra_req)