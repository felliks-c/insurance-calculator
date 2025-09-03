import requests

# response = requests.post(
#     "http://localhost:8000/notes/",
#     json={"text": "Пример другого текстового содержимого"}
# )
# print(response.text)
# response1 = requests.get("http://localhost:8000/notes/")
# print(response1.text)

# response2 = requests.get("http://localhost:8000/jwt/")
# print(response2.text)



response = requests.put("https://bima.tj", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}, json={"createAdmin": "123"})
print(response.status_code)
print(response.headers)