# Follow this post: https://realpython.com/api-integration-in-python/
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print(f"API get response from {api_url} ---> \n {response.json()}")
