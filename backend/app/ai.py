import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a medical translator."},
            {"role": "user", "content": f"Translate to {target_language}: {text}"}
        ]
    )
    return response.choices[0].message.content


def generate_summary(conversation_text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a medical assistant."},
            {"role": "user", "content": f"""
Summarize the medical conversation.
Highlight symptoms, diagnosis, medications, and follow-up steps.

Conversation:
{conversation_text}
"""}
        ]
    )
    return response.choices[0].message.content
