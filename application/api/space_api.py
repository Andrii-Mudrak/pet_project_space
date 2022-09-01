import requests

# example  https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

class SpaceAPI:

    def __init__(self, base_url:str, base_api:str, base_api_key:str):
        self.base_url = base_url
        self.base_api = base_api
        self.base_api_key = base_api_key

    def get_contain(self):
        r = requests.get(f"{base_url}{base_api}", params={'q': f"api_key={base_api_key}"})

