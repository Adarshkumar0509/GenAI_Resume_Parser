import os
import json
import re
from config import Config
from parser.groq_parser import call_groq_llm


class AIResumeParser:
    def __init__(self):
        # No OpenAI/Ollama dependencies — use Groq HTTP API
        self.model = os.getenv('GROQ_MODEL') or getattr(Config, 'GROQ_MODEL', None) or 'llama-4-scout'

    def extract_resume_data(self, resume_text: str) -> dict:
        prompt = self._create_extraction_prompt(resume_text)
        response_text = call_groq_llm(prompt, model=self.model)
        return self._parse_response(response_text)

    def _create_extraction_prompt(self, resume_text: str) -> str:
        return (
            "Extract the following fields from the resume text and output only valid minified JSON, "
            "with no explanation or extra text. Fields:\n"
            "{\"personal_information\": {\"name\": \"\", \"email\": \"\", \"phone\": \"\", \"address\": \"\"}, "
            "\"professional_summary\": \"\", \"skills\": [], \"work_experience\": [{\"company\": \"\", \"position\": \"\", \"duration\": \"\", \"responsibilities\": \"\"}], "
            "\"education\": [{\"institution\": \"\", \"degree\": \"\", \"field\": \"\", \"year\": \"\"}], \"certifications\": []}\n"
            f"Resume text:\n'''{resume_text}'''\n"
            "Respond ONLY with valid JSON having those keys, no comments, no explanations."
        )

    def _parse_response(self, response_text: str) -> dict:
        """Extract JSON from LLM response (handles code fences and plain JSON)."""
        def _extract_json_braces(text: str) -> str:
            """Find the first balanced JSON object in text and return it as a string.

            This scans for the first '{' and then finds the matching closing '}'
            while properly handling quoted strings and escape sequences so that
            braces inside strings don't break counting.
            """
            start = text.find('{')
            if start == -1:
                return None

            i = start
            depth = 0
            in_string = False
            escape = False
            while i < len(text):
                ch = text[i]
                if escape:
                    escape = False
                elif ch == '\\':
                    escape = True
                elif ch == '"':
                    in_string = not in_string
                elif not in_string:
                    if ch == '{':
                        depth += 1
                    elif ch == '}':
                        depth -= 1
                        if depth == 0:
                            return text[start:i+1]
                i += 1
            return None

        # If the response is already a Python dict/list, return it directly
        if isinstance(response_text, (dict, list)):
            return response_text

        # Normalize and try robust extraction
        response_text = (response_text or '').strip()

        # Remove common Markdown code fences if present
        # e.g. ```json\n{...}\n``` or ```\n{...}\n```
        code_fence_match = re.search(r'```(?:json)?\s*(.*?)\s*```', response_text, re.DOTALL | re.IGNORECASE)
        if code_fence_match:
            candidate = code_fence_match.group(1).strip()
        else:
            candidate = response_text

        # Try balanced-brace extraction (handles nested/braced text safely)
        json_str = _extract_json_braces(candidate)
        if not json_str:
            # fallback to simple regex that finds the first {...}
            m = re.search(r'\{[\s\S]*\}', candidate)
            json_str = m.group(0) if m else None

        if not json_str:
            # Nothing found
            print('Raw AI Response (no JSON found):', response_text)
            raise Exception(f'Failed to find a JSON object in AI response. Response: {response_text}')

        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print('Candidate JSON string:', json_str)
            print('Raw AI Response:', response_text)
            raise Exception(f'Failed to parse AI response as JSON: {str(e)}\nCandidate: {json_str}\nFull response: {response_text}')

