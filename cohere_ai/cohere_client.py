# cohere_ai/cohere_client.py

import cohere
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

def generate_completion(prompt: str, temperature: float = 0.7, max_tokens: int = 300):
    try:
        response = co.generate(
            model="command-r-plus",  # Use the latest free model
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print("Cohere generation failed:", e)
        return None
