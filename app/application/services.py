# El código de operaciones bancarias solamente.
#
# Tarea 1: Crea el servicio de transferencia interna (mismo banco).
# - Recibe cuenta origen, cuenta destino y monto.
# - Usa los métodos POO de tus objetos `Cuenta` para descontar y acreditar.
#
# Tarea 2: Crea el servicio de transferencia interbancaria (hacia otro contenedor).
# - ¿Cómo sabes si la cuenta destino pertenece a este banco o a otro? (mira los primeros 4 dígitos del número de cuenta y compáralos con `BANK_CODE`).
# - Si es de otro banco, descuenta el saldo localmente y usa `bank_client.py` para avisarle al otro contenedor por API.
