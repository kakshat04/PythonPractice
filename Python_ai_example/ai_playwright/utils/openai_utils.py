from openai import OpenAI
from config.prompts import prompts
import json
import os

def initialize_client():
    print(os.getcwd())
    with open(r"config\\openai_key.json") as f:
        api_key = json.load(f)["api_key"]
    return OpenAI(api_key=api_key)

def load_prompt(key):
    return prompts.get(key, "")

def generate_message(prompt):
    client = initialize_client()
    messages = [{
        "role": "user",
        "content": prompt,
    }]
    response =client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        max_tokens = 1000, 
        temperature=0.1, 
        top_p=1.0)
    return response.choices[0].message.content.strip()
