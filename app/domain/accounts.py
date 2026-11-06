# Aquí solo irá el código de Programación orientada a Objetos
# PROHIBIDO importar FastAPI, sqlite3 o librerías externas aquí, no hace falta.
#
# Tarea 1: Crea la clase base `Cuenta`.
# Preguntate:
# - ¿Qué atributos tienen las cuentas bancarias? (numero_cuenta, titular_id, saldo...).
# - Protege el atributo del saldo para que nadie pueda modificarlo haciendo `cuenta.saldo = 999999`.
# - Define métodos básicos: `depositar(monto)` y `retirar(monto)` validando que no se depositen números negativos.
#
# Tarea 2: Aplica Herencia y Polimorfismo.
# - Crea `CuentaAhorro(Cuenta)` y `CuentaCorriente(Cuenta)`.
# - Haz que el método `retirar(monto)` se comporte distinto en cada una (ej. una cobra comisión por retiro o permite sobregiro, y la otra no).
