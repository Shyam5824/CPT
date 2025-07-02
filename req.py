import requests
response= requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("status code:",response.status_code)
print("response json",response.json())