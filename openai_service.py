import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def summarize_text(text: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize calendar event details."},
            {"role": "user", "content": text}
        ]
    )
    return {"summary": response['choices'][0]['message']['content']}