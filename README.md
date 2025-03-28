# Gerenciador-de-Tarefas
Esse é o gerenciador de tarefas, desenvolvido em Python ele foi projetado para ajudar você a organizar suas atividades diárias. Este projeto utiliza uma abordagem de programação funcional, e foi elaborado como desafio da disciplina de Progamação Funcional do curso de Analise e Desenvolvimento de Sistemas da Unifor, essa abordagem permite que o código seja mais modular e fácil de manter.

## Descrição

O Gerenciador de Tarefas permite que você adicione, edite, remova e liste tarefas, além de marcar tarefas como concluídas. É uma aplicação útil para quem deseja acompanhar suas atividades de forma eficiente.

## Funcionalidades

- Adicionar novas tarefas
- Listar todas as tarefas
- Editar tarefas existentes
- Remover tarefas
- Marcar tarefas como concluídas
- Listar tarefas concluídas

## Tecnologias Utilizadas

- Python 3.13

## Estrutura do Projeto

```plaintext
gerenciamento_tarefas/
│
├── main.py               
├── tarefas/             
│   ├── __init__.py        
│   ├── tarefas.py         
│   └── utils.py           
│
├── usuarios/           
│   ├── __init__.py        
│   └── usuarios.py        
│
├── tests/                
│   ├── __init__.py        
│   ├── test_tarefas.py    
│   └── test_usuarios.py   
│  
└── requirements.txt

> ### 🔁 Passo-a-passo para fazer a clonagem do projeto (repositório)
```bash
# Comando para fazer a clonagem do repositório:
$ git clone https://github.com/CintiaBraulino/Gerenciador-de-Tarefas

# Acesse a pasta do projeto:
$ cd gerenciamento_tarefas

# Instale todas as dependências:
$ pip install -r requirements.txt

# Execute o comando abaixo para iniciar o servidor:
$ python main.py

# Comando para executar os teste:
$ python -m unittest discover -s tests


```

</br>

> ###  Equipe de desenvolvimento - 

<table align="center">
  <tr align="center">
    <td>
      <a href="https://github.com/CintiaBraulino">
        <img src="https://avatars.githubusercontent.com/CintiaBraulino" width=100 />
        <p>Cintia <br/>Braulino</p>
        <h1>Desenvolvedor/QA</h1>
      </a>
    </td>
    <td>
      <a href="https://github.com/Simonebraulino">
        <img src="https://avatars.githubusercontent.com/Simonebraulino" width=100 />
        <p>Simone <br/>Braulino</p>
        <h1>Analista de Requisitos/Desenvolvedor</h1>
      </a>
    </td>
  </tr>
</table>
