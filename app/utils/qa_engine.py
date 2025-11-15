import os
import requests

class QAEngine:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.model  = "gpt-4o"

    def ask_about_celebrity(self, name, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        prompt = f"""
You are an AI Assistant that knows a lot about celebrities. 
Answer the question about {name} concisely and accurately.

Question: {question}
"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.5,
            "max_tokens": 512
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]

        return "Sorry, I couldn't find the answer."
