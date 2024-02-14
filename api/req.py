# Follow this post: https://realpython.com/api-integration-in-python/
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print(f"API get response {api_url} ---> {response.json()}")

print(f"Reponse status {response.status_code}")
