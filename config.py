import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Groq configuration
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama-4-scout')
    GROQ_API_ENDPOINT = os.getenv('GROQ_API_ENDPOINT')

    # Legacy/OpenAI/Ollama fields kept for backward-compatibility (not used by this fork)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'llama3.2')

    @staticmethod
    def validate_api_key():
        if not Config.GROQ_API_KEY:
            print("Warning: GROQ_API_KEY not found in environment. Set GROQ_API_KEY to use the Groq API.")
