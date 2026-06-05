


CONTATOS = []

def cadastrar_contatos():
        nome = input("Digite o nome do contato:")
        numero = input("Digite o numero de telefone:")
        email = input("Digite o email do contato:")
        contato = {"Nome": nome, "Numero": numero, "Email": email, "Favorito": False}
        CONTATOS.append(contato)
        print(f"\nContato --> {nome} <-- adicionado com Sucesso! ")


def visualizar_contatos():
        for indice, contato in enumerate(CONTATOS, start=1):
            nome = contato["Nome"]
            email = contato["Email"]
            telefone = contato["Numero"]
            print("\nLista de Contatos")
            print()
            print(f"{indice}. ---> {nome} | {telefone} | {email}")
                

def atualizar_contatos():
    escolha = int(input("Qual contato deseja atualizar?:"))
    indice_corrigido = escolha -1 
    novo_nome = input("Digite o novo nome do contato:")
    novo_telefone = input("Digite o novo telefone do contato:")
    novo_email = input("Digite o novo email do contato:")
    CONTATOS[indice_corrigido]["Nome"] = novo_nome
    CONTATOS[indice_corrigido]["Numero"] = novo_telefone
    CONTATOS[indice_corrigido]["Email"] = novo_email
    print(f"Contato {escolha} atualizado para '{novo_nome}' com sucesso!")


def marcar_favorito():
    escolha = int(input("Qual contato deseja marcar como favorito?:"))
    indice_corrigido = escolha - 1 
    CONTATOS[indice_corrigido]["Favorito"] = True
    print(f"Contato {escolha} --> {CONTATOS[indice_corrigido]["Nome"]} Marcado como Favorito! ")


def visualizar_favoritos():
    for indice, contato in enumerate(CONTATOS):
            if contato["Favorito"] == True:
                nome = contato["Nome"]
                email = contato["Email"]
                telefone = contato["Numero"]
                print("Lista de contatos favoritos")
                print()
                print(f"{indice}. ---> {nome} | {telefone} | {email}")

def desmarcar_favorito():
    escolha = int(input("Qual contato voce deseja desfavoritar?:"))
    indice_corrigido = escolha -1 
    if CONTATOS[indice_corrigido]["Favorito"] == True:
        CONTATOS[indice_corrigido]["Favorito"] = False
        print("Contato desfavoritado")
    else:
        print("\nEsse contato não é um favorito!")
    

def deletar_contato():
    escolha = int(input("Qual contato voce deseja Deletar?:"))
    indice_corrigido = escolha -1 
    verificação = input("tem certeza que deseja Excluir este contato?(Sim/Não)")
    if verificação == "Sim":
        CONTATOS.pop(indice_corrigido)
        print("Contato Removido com Sucesso!")
    elif verificação == "Não":
        print("Nenhum contato foi deletado!")
    else:
        print("escolha invalida")

while True:
        print("\nMenu da agenda de Contatos") 
        print("\n1. Adicionar Contato")
        print("2. Ver contatos")
        print("3. Atualizar contatos")
        print("4. Marcar como favorito")
        print("5. Visualizar contatos favoritos")
        print("6. Desmarcar um Favorito")
        print("7. Deletar contato")
        print("8. Sair")
        try:
            escolha = int(input("Digite sua escolha: "))
        
            if escolha == 8:
                    print("Progarama finalizado")
                    break

            elif escolha == 1:
                cadastrar_contatos()

            elif escolha == 2:
                visualizar_contatos()

            elif escolha == 3:
                visualizar_contatos()
                atualizar_contatos()

            elif escolha == 4:
                visualizar_contatos()
                marcar_favorito()

            elif escolha == 5:
                visualizar_favoritos()

            elif escolha == 6:
                print("Seus contatos favoritos")
                visualizar_favoritos()
                desmarcar_favorito()

            elif escolha == 7:
                visualizar_contatos()
                deletar_contato()
        except:
            print("Ocorreu um erro")