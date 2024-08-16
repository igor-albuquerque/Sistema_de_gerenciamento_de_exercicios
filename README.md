# Sistema de Gerenciamento de Exercícios
## Objetivo
Criação de um sistema básico de gerenciamento de exercícios com as seguintes funcionalidades:
- Fazer login e cadastrar professores e alunos.
- Pesquisar exercícios por tipo de questão, por matéria ou sortear exercícios aleatórios.
- Listar todos os exercícios disponíveis no sistema.
- Caso o usuário seja um professor, é possível cadastrar exercícios dissertativos, de múltipla escolha, de verdadeiro ou falso ou atualizar os exercícios já cadastrados.
- Caso o usuário seja um aluno, é possível responder as questões cadastradas no sistema e receber um feedback (Ver os acertos e erros).
- Os professores tem acesso ao feedback de todos os alunos e à visualização das respostas de questões dissertativas.

## Tecnologias e Ferramentas Usadas
- Linguagem de programação: Python.
- Bibliotecas usadas: os, random, pymongo.
- Banco de dados: MongoDB.

## Necessidades para Funcionamento
- Endereço do banco MongoDB na classe Connection.
- Banco de dados chamado 'AC4' ou mudar o nome do banco na classe Connection.
- Dentro do banco, ter as coleções 'Cadastro', 'Dissertativas', 'Exercicios' e 'Feedback'.

## Contribuidores
- Leticia Queiroz (https://github.com/LeticiaQueiroz57)
- João Basílio (https://github.com/joaobasilio77)
- Igor Albuquerque (https://github.com/igor-albuquerque)
