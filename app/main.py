import os
from fastapi import FastAPI

bank_name = os.getenv("BANK_NAME", "Banco Desconocido")
bank_code = os.getenv("BANK_CODE", "0000")

app = FastAPI(title=f"API de {bank_name} ({bank_code})")


@app.get("/")
def health_check():
    return {
        "status": "online",
        "banco": bank_name,
        "codigo": bank_code,
        "mensaje": "El contenedor está vivo. ¡Ahora construye el sistema!",
    }


# Tarea: Importa y conecta aquí tus rutas desde `app/presentation/routes.py`
