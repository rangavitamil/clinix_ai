import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env file")


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def get_ai_response(user_message):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_message
    )

    return response.text