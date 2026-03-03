import sys
import os
import uvicorn

# Adiciona o diretório atual ao path para que o pacote 'api' seja encontrado
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
