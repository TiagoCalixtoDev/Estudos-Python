# Lista de usuários bloqueados
usuarios_bloqueados = ['joao', 'maria']

# Entrada de dados
nome = input("Digite seu nome: ").lower().strip()
idade = int(input("Digite sua idade: "))
tem_cnh = input("Você tem CNH? (sim/não): ").lower().strip()
saldo = float(input("Digite seu saldo: "))

# Verificações
if (
    idade >= 18
    and tem_cnh == 'sim'
    and nome not in usuarios_bloqueados
    and saldo > 0
):
    print(f"Acesso permitido para {nome}")
elif nome in usuarios_bloqueados or saldo <= 0:
    print(f"Acesso negado para {nome}")
else:
    print("Dados insuficientes para liberar acesso")
