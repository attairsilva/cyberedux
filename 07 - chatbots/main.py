import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv() 

client = Groq(
    api_key=os.getenv('GROQ_KEY'),
)

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explique em portugues a importância dos modelos de linguagem rápida",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat.choices[0].message.content)