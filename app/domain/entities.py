# Entidades base del sistema.
# PROHIBIDO usar FastAPI, diccionarios JSON o librerías externas aquí. Pura lógica de programación, diagramas de flujo.
#
# Tarea 1: Crea la clase `Cliente`.
# - Piensa: ¿Qué datos identifican a un cliente en el mundo real? (ej. id, nombre, documento, email).
#
# Tarea 2: Crea la clase `Banco`.
# - Solo necesita representar la institución: nombre y código identificador (ej. '0101').
#
# Tarea 3: Crea la clase `Transaccion`.
# - Esta clase será el registro inmutable de un movimiento de dinero.
# - Debe contener al menos: id_transaccion, cuenta_origen, cuenta_destino, monto, fecha_hora, y tipo (deposito, retiro, transferencia).
