import os
from dotenv import load_dotenv


# Load .env file
load_dotenv()


LLM_URL = os.getenv("LLM_URL")

LLM_API_KEY = os.getenv("LLM_API_KEY")

LLM_MODEL = os.getenv("LLM_MODEL")