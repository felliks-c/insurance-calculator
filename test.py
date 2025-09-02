import requests

response = requests.post(
    "http://localhost:8000/notes/",
    json={"text": "Пример другого текстового содержимого"}
)
print(response.text)
response1 = requests.get("http://localhost:8000/notes/")
print(response1.text)

response2 = requests.get("http://localhost:8000/jwt/")
print(response2.text)