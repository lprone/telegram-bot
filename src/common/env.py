import os

from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv('TELEGRAM_TOKEN')
groq_key = os.environ.get("GROQ_API_KEY")
llm_model = os.environ.get("GROQ_LLM_MODEL")