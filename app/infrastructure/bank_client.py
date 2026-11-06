#  Comunicación con el mundo exterior (Otros bancos)(contenedores Docker).
#
# Tarea 1: Importa la librería `httpx` para hacer peticiones HTTP.
# Tarea 2: Lee la variable de entorno `PEER_BANK_URL` usando `os.getenv()`.
# Tarea 3: Crea la función/clase `enviar_transferencia_externa(cuenta_origen, cuenta_destino, monto)`.
# - Debes crear un diccionario (que luego será JSON) con los datos del envío. (Investigar comunicacion HTTP)
# - Debes hacer una petición HTTP POST hacia el `PEER_BANK_URL`.
# - Manejo de errores: ¿Qué pasa si el otro contenedor de Docker está apagado? Atrapa la excepción y devuelve un error amigable en lugar de crashear el banco.
