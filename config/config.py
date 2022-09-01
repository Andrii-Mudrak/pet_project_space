from confidential import Secret


class Config:
    
    base_api_key = Secret.key
    base_url = 'https://api.nasa.gov/planetary/'
    base_api = 'apod'