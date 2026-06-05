

TAREFAS = []


def criar_tarefa():
    nome_tarefa = input("Digite um nome pra sua tarefa:")
    descrição_tarefa = input ("digite uma descrição para essa tarefa:")
    tarefa = {"nome": nome_tarefa, "descrição":descrição_tarefa, "Completada": False}
    print(f"Tarefa  '{nome_tarefa}'  adicionada com Sucesso")
    TAREFAS.append(tarefa)
    return TAREFAS


def visualizar_tarefas():
    print ("\nLista de Tarefas")
    for indice, tarefa in enumerate(TAREFAS, start=1):
        status = "✓" if tarefa ["Completada"] else " "
        nome_tarefa = tarefa["nome"]
        Descrição_tarefa = tarefa["descrição"]
        print(f"{indice}. [{status}]  {nome_tarefa} --->  Descrição: {Descrição_tarefa}")


def atualizar_tarefas():
    indice_tarefa = int(input("Digite o numero da tarefa que deseja atualizar :"))
    indice_tarefa_atualizado = indice_tarefa - 1
    novo_nome = input("\nDigite o novo nome da tarefa:")
    nova_descrição = input ("Digite a nova descrição da tarefa:")
    print (f"Tarefa {indice_tarefa_atualizado} Atualizada para {novo_nome}")
    TAREFAS[indice_tarefa_atualizado]["nome"] = novo_nome
    TAREFAS[indice_tarefa_atualizado]["descrição"] = nova_descrição
    print("\nTarefa atualizada com sucesso!")


def completar_tarefa():
    tarefa = int(input("Digite o numero da tarefa que desejar marcar como completa:"))
    indice_tarefa = tarefa -1
    TAREFAS[indice_tarefa]["Completada"] = True
    nome = TAREFAS[indice_tarefa]["nome"]
    print(f"Tarefa '{nome}' ---> COMPLETA COM SUCESSSO!!!")


def deletar_tarefas_completadas():
    escolha = input("Deseja realmente excluir todas as tarefas completadas? (Sim/Não)")
    if escolha == "Sim":
        for tarefa in TAREFAS:
            if tarefa["Completada"] == True:
                TAREFAS.remove(tarefa)
    elif escolha == "Não":
        print ("Nenhuma Tarefa foi excluida")
    else:
        print("Escolha invalida")

def deletar_tarefa_especifica():
    indice_tarefa = int(input("Deseja excluir qual tarefa ? "))
    indice_tarefa_atualizado = indice_tarefa - 1
    escolha = input(f"Deseja realmente excluir a tarefa '{TAREFAS[indice_tarefa]["nome"]}'? (Sim/Não)")
    if escolha == "Sim":
            TAREFAS.remove(TAREFAS[indice_tarefa_atualizado])
            print(f"Tarefa {TAREFAS["nome"]} Excluida com sucesso! ")
    elif escolha == "Não":
        print("Nenhuma tarefa foi excluida")
    else:
        print("Escolha invalida")

while True:
    print("\nMenu do gerenciador de lista de tarefas") 
    print("\n1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefas")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Deletar tarefa especifica")
    print("7. Sair")

    escolha = int(input("Digite sua escolha:"))
    try:
        if escolha == 7:
            print("Progarama finalizado")
            break

        elif escolha == 1:
            criar_tarefa()
            
        elif escolha == 2:
            visualizar_tarefas()

        elif escolha == 3:
            visualizar_tarefas()
            atualizar_tarefas()
            visualizar_tarefas()

        elif escolha == 4:
            visualizar_tarefas()
            completar_tarefa()

        elif escolha == 5:
            visualizar_tarefas()
            deletar_tarefas_completadas()

        elif escolha == 6:
                visualizar_tarefas()
                deletar_tarefa_especifica()

        else:
            print ("escolha invalida")
    except:
        print("Ocorreu um erro")