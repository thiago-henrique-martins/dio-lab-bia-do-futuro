import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env local
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY não encontrada. Verifique o arquivo .env")