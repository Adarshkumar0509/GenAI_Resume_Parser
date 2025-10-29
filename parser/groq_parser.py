import os
import requests
from dotenv import load_dotenv

load_dotenv()


def call_groq_llm(prompt: str, model: str = None) -> str:
    """Call Groq's chat completions endpoint and return assistant text.

    Uses environment variables:
      - GROQ_API_KEY
      - GROQ_MODEL (optional, default: 'llama-4-scout')
      - GROQ_API_ENDPOINT (optional)
    """
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        raise Exception('GROQ_API_KEY is not set in environment')

    # Allow caller to override model parameter
    model = model or os.getenv('GROQ_MODEL', 'llama-4-scout')
    # Use Groq's OpenAI-compatible Responses API by default
    endpoint = os.getenv('GROQ_API_ENDPOINT', 'https://api.groq.com/openai/v1/responses')

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': model,
        'input': prompt,
        'temperature': 0.1,
        'max_output_tokens': 1500
    }

    resp = requests.post(endpoint, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    # Groq Responses API returns an 'output' array; extract assistant text from
    # items with type 'message' and content entries of type 'output_text'. If
    # not found, fall back to other common shapes.
    outputs = data.get('output', [])
    texts = []
    for out in outputs:
        for c in out.get('content', []):
            if c.get('type') in ('output_text', 'message') and 'text' in c:
                texts.append(c['text'])
            # some items use 'text' at top-level in content
            elif c.get('type') == 'reasoning_text' and 'text' in c:
                texts.append(c['text'])

    if texts:
        return '\n'.join(texts)

    # Fallbacks for OpenAI-like shapes
    if 'choices' in data:
        try:
            return data['choices'][0]['message']['content']
        except Exception:
            try:
                return data['choices'][0]['text']
            except Exception:
                pass

    raise Exception(f'Unexpected Groq response shape: {data}')
