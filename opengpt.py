import requests

class OpenGPT:
    def __init__(self):
        self.base_url = "http://api.opengpt-project.org"

    def make_request(self, user_input):
        endpoint = f"{self.base_url}/api/openai/default"
        data = {"user_input": user_input}

        try:
            response = requests.post(endpoint, json=data)

            if response.status_code == 200:
                return response.json().get("assistant_reply")
            elif response.status_code == 429:
                print("Rate limit exceeded. Try again later.")
            else:
                print(f"Error: {response.status_code}, {response.json()}")
                return None

        except requests.exceptions.RequestException as e:
            return None
