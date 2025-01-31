import requests
from requests.auth import HTTPBasicAuth

def list_exchanges():
    # RabbitMQ management API details
    host = "http://localhost:8080"  # Replace with your RasbbitMQ server address
    api_endpoint = f"{host}/api/exchanges"
    username = "guest"  # Replace with RabbitMQ username
    password = "guest"  # Replace with RabbitMQ password

    # Make an API request
    response = requests.get(api_endpoint, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        exchanges = response.json()
        print("List of Exchanges:")
        for exchange in exchanges:
            print(f"- Name: {exchange['name']}, Type: {exchange['type']}")
    else:
        print(f"Failed to fetch exchanges. HTTP Status: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    list_exchanges()
