import openai
import os
from dotenv import load_dotenv

class OpenAIAPI:
    def __init__(self, api_key: str=None) -> None:
        if api_key is None:
            load_dotenv()
            api_key = os.getenv('OPENAI_KEY')
        openai.api_key = api_key
        self._custom_instruction: str = None

