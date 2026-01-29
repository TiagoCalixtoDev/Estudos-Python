saldo = 1000
saque = 300
hora_atual = 10
LIMITE_SAQUE = 500

saque_dentro_limite = saque <= LIMITE_SAQUE
saldo_suficiente = saque <= saldo
horario_permitido = hora_atual >= 6 and hora_atual <= 22

saque_autorizado = (
    saque_dentro_limite and
    saldo_suficiente and
    horario_permitido
)

if saque_autorizado:
    print('Saque Permitido')
else:
    print('Saque bloqueado')
