import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Translate medical text to {target_lang}"},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content

    except openai.error.RateLimitError:
        # Fallback response
        return f"[Translation unavailable due to API quota] Original text: {text}"


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
