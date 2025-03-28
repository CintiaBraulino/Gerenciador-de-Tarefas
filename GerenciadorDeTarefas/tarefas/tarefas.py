from typing import List, Dict

# Simulação de "banco de dados" para as tarefas
tarefas_db: List[Dict] = []

def contador_tarefas():
    """Closure para contar quantas tarefas foram adicionadas."""
    count = 0

    def adicionar_tarefa_contada(titulo: str, descricao: str):
        nonlocal ccount
        count += 1
        tarefa = {
            'id': count,
            'titulo': titulo,
            'descricao': descricao,
            'concluida': False
        }
        tarefas_db.append(tarefa)
    
    return adicionar_tarefa_contada

# Cria a função de contar tarefas
adicionar_tarefa = contador_tarefas()

def listar_tarefas() -> List[Dict]:
    """Lista todas as tarefas cadastradas."""
    return tarefas_db

def listar_tarefas_nao_concluidas() -> List[Dict]:
    """Listar tarefas que não estão concluídas usando list comprehension."""
    return [tarefa for tarefa in tarefas_db if not tarefa['concluida']]

def ordenar_tarefas_por_titulo() -> List[Dict]:
    """Ordena as tarefas pelo título, usando uma função lambda."""
    return sorted(tarefas_db, key=lambda tarefa: tarefa['titulo'])

def editar_tarefa(tarefa_id: int, novo_titulo: str, nova_descricao: str):
    """Edita os detalhes de uma tarefa existente."""
    for tarefa in tarefas_db:
        if tarefa['id'] == tarefa_id:
            tarefa['titulo'] = novo_titulo
            tarefa['descricao'] = nova_descricao
            return
    print(f"Tarefa ID {tarefa_id} não encontrada.")

def remover_tarefa(tarefa_id: int):
    """Remove uma tarefa da lista."""
    global tarefas_db
    tarefas_db = [tarefa for tarefa in tarefas_db if tarefa['id'] != tarefa_id]

def marcar_tarefa_concluida(tarefa_id: int):
    """Marca uma tarefa como concluída."""
    for tarefa in tarefas_db:
        if tarefa['id'] == tarefa_id:
            tarefa['concluida'] = True
            return
    print(f"Tarefa ID {tarefa_id} não encontrada.")

def listar_tarefas_concluidas() -> List[Dict]:
    """Retorna uma lista de tarefas que estão concluídas."""
    return [tarefa for tarefa in tarefas_db if tarefa['concluida']]