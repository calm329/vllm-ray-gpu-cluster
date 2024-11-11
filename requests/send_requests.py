import requests
from concurrent.futures import ThreadPoolExecutor
import time

url = "http://10.0.0.6:30080/v1/completions"
payload = {
            "model": "/app/mistral-7b-instruct-v0.2-code-ft.Q4_K_S.gguf",
            "prompt": "San Francisco is a",
            "max_tokens": 7,
            "temperature": 0
}

# Function to send a single request and measure response time
def send_request():
    start_time = time.time()
    try:                   
        response = requests.post(url, json=payload, timeout=10)  # 10 seconds timeout
        end_time = time.time()
        print("Response:", response.text)  # Print raw response to capture any errors
        print(f"Time taken: {end_time - start_time:.2f} seconds")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
                                
# Sequential test to ensure basic functionality
print("Testing single request...")
send_request()
# Send 10 requests in parallel       
print("\nTesting parallel requests...")
with ThreadPoolExecutor(max_workers=40) as executor:
    for _ in range(40):
        executor.submit(send_request)
