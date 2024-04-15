<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 1

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar um programa que implementa a funcionalidade "Listar todos os cadastros" de um sistema de cadastro de dados pessoais conforme a descrição a seguir.

## Armazenamento dos cadastros

Cada cadastro é composto pelos seguintes dados de uma pessoa:

- **ID**: Nº inteiro positivo que identifica cada cadastro. Esse nº corresponderá à posição de cada cadastro na estrutura de armazenamento. Ou seja, o ID do 1º cadastro será 1, o do 2º será 2 e assim sucessivamente.
- **Nome**: Composto por primeiro nome e um único sobrenome (ex: José Silva).
- **CPF**: Composto por 11 dígitos (ex: 99999999999).
- **Data de nascimento**: No formato dd/mm/aaaa (ex: 01/02/1999).

Os dados dos cadastros devem ser armazenados em listas.

## Descrição das funcionalidades

### Listar todos os cadastros

O programa deverá apresentar todos os cadastros armazenados, detalhando para cada um os dados correspondentes (ID, nome, CPF e data de nascimento) com uma formatação adequada para sua visualização.

Caso não haja nenhum cadastro armazenado, o programa deverá imprimir uma mensagem com esta informação.

*Observações:*

- O arquivo main.py já contém definições de listas que podem ser usadas para o armazenamento dos dados dos cadastros, mas você pode alterá-las como julgar apropriado.
- Você pode alterar o conteúdo das listas manualmente, inserindo alguns dados para realizar testes.