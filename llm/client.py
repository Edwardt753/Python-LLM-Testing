import requests

from config.settings import (
    LLM_URL,
    LLM_API_KEY,
    LLM_MODEL
)



def send_to_llm(prompt):

    payload = {
        "model": LLM_MODEL,
        "prompt": prompt
    }


    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }


    response = requests.post(
        LLM_URL,
        json=payload,
        headers=headers
    )


    response.raise_for_status()


    data = response.json()


    return data["response"]