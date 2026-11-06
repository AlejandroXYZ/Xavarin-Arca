# Endpoints de la API y validación de entrada/salida (Fronteras)
# Aquí SÍ debes importar FastAPI, APIRouter y crear modelos de Pydantic.
#
# Tarea 1: Crea un `APIRouter()` para agrupar tus rutas.
# Tarea 2: Crea modelos Pydantic (BaseModel) para validar los datos de entrada (Ej. `TransferenciaRequest`). Te recomiendo crear los modelos pydantic en otro archivo o otra carpeta llamada schemas
#
# Tarea 3: Crea el Endpoint POST `/clientes`: Recibe datos y usa los servicios de Aplicación para crear el cliente.
# Tarea 4: Crea el Endpoint GET `/cuentas/{numero_cuenta}`: Devuelve el saldo actual.
#
# Tarea 5: Endpoint POST `/transferencias`:
# - Recibe el origen, destino y monto.
# - Llama a tu capa de Aplicación (`services.py`).
# - Devuelve código HTTP 200 si es exitosa, o lanza `HTTPException(status_code=400)` si el dominio rechazó la operación (ej. fondos insuficientes).
#
# Tarea 6 (Fase 4): Endpoint POST `/api/transferencias-entrantes`.
# - Esta es la frontera o puerta que recibirá las peticiones de los OTROS contenedores cuando te envíen dinero. Solo va a recibir si el contenedor está activo escuchando
