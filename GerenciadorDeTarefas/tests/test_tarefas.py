
import unittest
from tarefas.tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    editar_tarefa,
    remover_tarefa,
    listar_tarefas_nao_concluidas,
    listar_tarefas_concluidas
)

class TestTarefas(unittest.TestCase):
    def setUp(self):
        """Configura os testes com uma tarefa inicial."""
        adicionar_tarefa('Tarefa Teste', 'Descrição da tarefa de teste')

    def test_adicionar_tarefa(self):
        """Testa se a tarefa é adicionada corretamente."""
        tarefas = listar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]['titulo'], 'Tarefa Teste')

    def test_editar_tarefa(self):
        """Testa se a tarefa é editada corretamente."""
        editar_tarefa(1, 'Tarefa Editada', 'Descrição da tarefa editada')
        tarefa = listar_tarefas()[0]
        self.assertEqual(tarefa['titulo'], 'Tarefa Editada')

    def test_remover_tarefa(self):
        """Testa se a tarefa é removida corretamente."""
        remover_tarefa(1)
        tarefas = listar_tarefas()
        self.assertEqual(len(tarefas), 0)

    def test_listar_tarefas_nao_concluidas(self):
        """Testa a listagem de tarefas não concluídas."""
        tarefas_nao_concluidas = listar_tarefas_nao_concluidas()
        self.assertEqual(len(tarefas_nao_concluidas), 1)

    def test_listar_tarefas_concluidas(self):
        """Testa a listagem de tarefas concluídas."""
        # Primeiro, vamos concluir a tarefa
        marcar_tarefa_concluida(1)
        tarefas_concluidas = listar_tarefas_concluidas()
        self.assertEqual(len(tarefas_concluidas), 1)

if __name__ == "__main__":
    unittest.main()