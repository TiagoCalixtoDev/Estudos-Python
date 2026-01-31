nome = input("Digite seu nome: ").strip()

if nome.isalpha():
    tamanho_nome = len(nome)

    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif 5 <= tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite apenas letras")
