import os
from dotenv import load_dotenv

load_dotenv()

# OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
# OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:20b-cloud") se usa o modelo com 20 bilhões na nuvens

# config.py
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b") # 20b não rodará nos seus 4GB de RAM
