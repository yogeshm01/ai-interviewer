import requests

api_url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer dummy_key"}

response = requests.post(api_url, headers=headers, json={"inputs": ["hello"]})
print("Status code:", response.status_code)
print("Response text:", response.text)
