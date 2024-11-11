import requests
import json

# Endpoint and headers
url = "http://10.0.0.29:30080/v1/completions"
headers = {
            "Content-Type": "application/json"
}

# Define all prompts in one list
base_prompts = [
            "San Francisco is a",
            "The future of AI is",
            "The capital of France is",
            "Machine learning is transforming",
            "The fastest land animal is",
            "The inventor of the light bulb is",
            "The tallest mountain on Earth is",
            "Climate change affects",
            "Quantum computing is",
            "The most widely spoken language is",
]

# Total number of prompts desired
total_prompts = 100

# Repeat the base prompts until reaching the desired number of prompts
prompts = (base_prompts * (total_prompts // len(base_prompts) + 1))[:total_prompts]

# Define the payload for all prompts
payload = {
            "model": "/app/mistral-7b-instruct-v0.2-code-ft.Q4_K_S.gguf",
            "prompt": prompts,
            "max_tokens": 50,
            "temperature": 0.8
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Process and print each prompt and response text
if response.status_code == 200:
    response_json = response.json()
    for i, choice in enumerate(response_json['choices']):
        prompt = prompts[i]
        generated_text = choice['text']
        print(f"Prompt: {prompt}")                                                
        print(f"Response: {generated_text}")
        print("-" * 50)
else:
    print(f"Failed to get response. Status code: {response.status_code}")

