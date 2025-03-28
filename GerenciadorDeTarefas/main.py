from tarefas.tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    listar_tarefas_nao_concluidas,
    ordenar_tarefas_por_titulo,
    editar_tarefa,
    remover_tarefa,
    marcar_tarefa_concluida,
    listar_tarefas_concluidas
)

def mostrar_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Listar Tarefas Não Concluídas")
    print("4. Editar Tarefa")
    print("5. Remover Tarefa")
    print("6. Marcar Tarefa como Concluída")
    print("7. Listar Tarefas Concluídas")
    print("8. Listar Tarefas Ordenadas por Título")
    print("0. Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            adicionar_tarefa(titulo, descricao)
            print("Tarefa adicionada com sucesso!")
        elif opcao == "2":
            print("Lista de Tarefas:")
            for tarefa in listar_tarefas():
                print(tarefa)
        elif opcao == "3":
            print("Tarefas Não Concluídas:")
            for tarefa in listar_tarefas_nao_concluidas():
                print(tarefa)
        elif opcao == "4":
            tarefa_id = int(input("ID da Tarefa a ser editada: "))
            novo_titulo = input("Novo Título: ")
            nova_descricao = input("Nova Descrição: ")
            editar_tarefa(tarefa_id, novo_titulo, nova_descricao)
            print("Tarefa editada com sucesso!")
        elif opcao == "5":
            tarefa_id = int(input("ID da Tarefa a ser removida: "))
            remover_tarefa(tarefa_id)
            print("Tarefa removida com sucesso!")
        elif opcao == "6":
            tarefa_id = int(input("ID da Tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(tarefa_id)
            print("Tarefa marcada como concluída!")
        elif opcao == "7":
            print("Tarefas Concluídas:")
            for tarefa in listar_tarefas_concluidas():
                print(tarefa)
        elif opcao == "8":
            print("Tarefas Ordenadas por Título:")
            for tarefa in ordenar_tarefas_por_titulo():
                print(tarefa)
        elif opcao == "0":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()