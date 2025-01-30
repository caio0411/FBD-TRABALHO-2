# Trabalho Prático II - Desenvolvimento de Aplicações para Bancos de Dados

## Índice

1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Instalação](#instalação)
4. [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
5. [Execução dos Scripts](#execução-dos-scripts)
   - [1. Criação das Tabelas](#1-criação-das-tabelas)
   - [2. Inserção de Dados](#2-inserção-de-dados)
   - [3. Execução das Consultas](#3-execução-das-consultas)
   - [4. Manipulação de Transações](#4-manipulação-de-transações)
   - [5. Procedimento Armazenado](#5-procedimento-armazenado)
   - [6. Implementação de Gatilhos (Triggers)](#6-implementação-de-gatilhos-triggers)
6. [Verificação e Apresentação](#verificação-e-apresentação)
7. [Estrutura de Arquivos](#estrutura-de-arquivos)
8. [Dicas Finais](#dicas-finais)
9. [Contato para Dúvidas](#contato-para-dúvidas)

---

## Introdução

Este documento serve como guia para a execução dos scripts desenvolvidos no **Trabalho Prático II** da disciplina de **Desenvolvimento de Aplicações para Bancos de Dados**. Os scripts, desenvolvidos em Python e PL/pgSQL, interagem com um banco de dados PostgreSQL para realizar diversas operações, incluindo criação de tabelas, inserção de dados, consultas, transações, procedimentos armazenados e gatilhos.

## Requisitos

- **Python 3** instalado na máquina.
- **Módulo psycopg3** para Python.
- Acesso ao servidor PostgreSQL com as credenciais fornecidas:
  - **Host:** `200.129.44.249`
  - **Database:** Mesmo utilizado no Trabalho Prático I
  - **User:** `suaMatricula`
  - **Senha:** `suaMatricula`

## Instalação

### 1. Instalação do Python 3

Caso ainda não tenha o Python 3 instalado, siga os tutoriais abaixo de acordo com o seu sistema operacional:

- **Windows:** [Instalação no Windows](https://python.org.br/instalacao-windows/)
- **Linux:** [Instalação no Linux](https://python.org.br/instalacao-linux/)

### 2. Instalação do Módulo psycopg3

Abra o terminal ou prompt de comando e execute:

```bash
pip install psycopg
```

Para mais detalhes e guias de uso, consulte a [documentação do psycopg3](https://www.psycopg.org/psycopg3/docs/).

## Configuração do Banco de Dados

Nos scripts Python fornecidos, configure a conexão com o banco de dados utilizando as credenciais fornecidas:

```python
import psycopg

conn = psycopg.connect(
    host="200.129.44.249",
    database="nome_do_banco",  # Substitua pelo banco usado no Trabalho Prático I
    user="suaMatricula",
    password="suaMatricula"
)
```

## Execução dos Scripts

### 1. Criação das Tabelas

**Script:** `cria_tabelas.py`

**Descrição:** Cria as tabelas necessárias no banco de dados conforme o esquema fornecido.

**Como Executar:**

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde está o script `cria_tabelas.py`.
3. Execute o script:

   ```bash
   python cria_tabelas.py
   ```

**Verificação:** Acesse o PostgreSQL (usando pgAdmin ou linha de comando) para confirmar a criação das tabelas.

### 2. Inserção de Dados

**Script:** `insere_dados.py`

**Descrição:** Insere os dados fornecidos nas respectivas tabelas do banco de dados.

**Como Executar:**

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde está o script `insere_dados.py`.
3. Execute o script:

   ```bash
   python insere_dados.py
   ```

**Verificação:** Verifique no PostgreSQL se os dados foram inseridos corretamente nas tabelas.

### 3. Execução das Consultas

**Script:** `consultas.py`

**Descrição:** Executa consultas específicas no banco de dados e exibe os resultados.

**Consultas Realizadas:**
- Retorna todas as turmas e a quantidade de alunos participantes de cada turma.
- Retorna os alunos matriculados na disciplina de “Fundamentos de Bancos de Dados”.
- Retorna a quantidade de professores do curso de “Ciências da Computação”.

**Como Executar:**

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde está o script `consultas.py`.
3. Execute o script:

   ```bash
   python consultas.py
   ```

**Verificação:** Observe os resultados das consultas no terminal para garantir que estão corretos.

### 4. Manipulação de Transações

**Script:** `transacao.py`

**Descrição:** Realiza operações em uma única transação, atualizando o estado de uma turma e removendo matrículas de alunos.

**Operações Realizadas:**
1. Atualiza o estado da turma “CC2024DS1” para “Fechado”.
2. Remove todas as matrículas de alunos na turma “CC2024DS1” na tabela Aluno Turma.

**Como Executar:**

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde está o script `transacao.py`.
3. Execute o script:

   ```bash
   python transacao.py
   ```

**Verificação:** Verifique no PostgreSQL se o estado da turma foi atualizado e as matrículas removidas conforme esperado.

### 5. Procedimento Armazenado

#### 5.1. Criação do Procedimento Armazenado

**Arquivo:** `inc_semestre.sql`

**Descrição:** Cria um procedimento armazenado que incrementa o semestre dos alunos.

**Como Executar:**

1. Abra o pgAdmin ou qualquer cliente SQL que você use.
2. Abra o arquivo `inc_semestre.sql`.
3. Execute o script para criar o procedimento no banco de dados.

#### 5.2. Execução do Script Python para Chamar o Procedimento

**Script:** `chama_procedimento.py`

**Descrição:** Chama o procedimento armazenado `inc_semestre` passando o valor 1 como parâmetro.

**Como Executar:**

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde está o script `chama_procedimento.py`.
3. Execute o script:

   ```bash
   python chama_procedimento.py
   ```

**Verificação:** Verifique se os semestres dos alunos foram incrementados corretamente no banco de dados.

### 6. Implementação de Gatilhos (Triggers)

#### 6.1. Criação dos Gatilhos no Banco de Dados

**Arquivos:** `gatilho_capacidade.sql` e `gatilho_disciplinas.sql`

**Descrição:** Implementa gatilhos que:
1. Garantem que o número de alunos matriculados em uma turma não exceda a capacidade máxima.
2. Restringem um aluno a não cursar mais do que 4 disciplinas em um semestre.

**Como Executar:**

1. Abra o pgAdmin ou qualquer cliente SQL que você use.
2. Abra o arquivo `gatilho_capacidade.sql` e execute o script.
3. Abra o arquivo `gatilho_disciplinas.sql` e execute o script.

#### 6.2. Execução dos Scripts Python para Testar os Gatilhos

**Scripts:**
- `insere_aluno_turma_tabela7.py`
- `insere_aluno_turma_tabela8.py`

**Descrição:** Tenta inserir tuplas na tabela "Aluno Turma" conforme as Tabelas 7 e 8, testando os gatilhos implementados.

**Como Executar:**

1. **Para a Tabela 7:**

   - Navegue até o diretório onde está o script `insere_aluno_turma_tabela7.py`.
   - Execute:

     ```bash
     python insere_aluno_turma_tabela7.py
     ```

2. **Para a Tabela 8:**

   - Navegue até o diretório onde está o script `insere_aluno_turma_tabela8.py`.
   - Execute:

     ```bash
     python insere_aluno_turma_tabela8.py
     ```

**Verificação:** Observe as mensagens de erro ou sucesso no terminal para confirmar se os gatilhos estão funcionando corretamente (por exemplo, prevenindo exceder a capacidade da turma ou limitando o número de disciplinas por semestre).

## Verificação e Apresentação

### 1. Verificar Todos os Componentes

- **No PostgreSQL e Ambiente Local:**
  - Revise cada tabela para garantir que os dados estão consistentes.
  - Execute manualmente algumas consultas no pgAdmin para validar os resultados.
  - Revise os logs dos scripts Python para assegurar que todas as operações foram concluídas com sucesso.

### 2. Preparar a Apresentação

- **Organização dos Arquivos:**
  - Organize os scripts Python e os arquivos `.sql` em um único diretório.
- **Compressão dos Arquivos:**
  - Comprimir o diretório em um arquivo `.zip` seguindo o formato requerido:
    ```
    FBD_Trabalho_II_NomeAluno1_NomeAluno2.zip
    ```
- **Envio:**
  - Faça o upload do arquivo `.zip` no Google Classroom antes do prazo estipulado.

### 3. Preparar-se para a Arguição

- **Explicação da Ordem de Execução:**
  - Esteja pronto para explicar a sequência lógica de execução dos scripts.
- **Demonstração:**
  - Mostre a conexão entre os scripts Python e o banco de dados PostgreSQL.
- **Implementação de Gatilhos e Procedimentos Armazenados:**
  - Explique como foram implementados e testados.
- **Exemplos:**
  - Tenha exemplos de saídas e possíveis erros que foram tratados nos scripts.

## Estrutura de Arquivos

- **Scripts Python:**
  - `cria_tabelas.py`
  - `insere_dados.py`
  - `consultas.py`
  - `transacao.py`
  - `chama_procedimento.py`
  - `insere_aluno_turma_tabela7.py`
  - `insere_aluno_turma_tabela8.py`
- **Arquivos SQL:**
  - `inc_semestre.sql`
  - `gatilho_capacidade.sql`
  - `gatilho_disciplinas.sql`
- **Comprimido:**
  - `FBD_Trabalho_II_NomeAluno1_NomeAluno2.zip`

## Dicas Finais

- **Teste Individualmente:** Execute cada script individualmente e verifique os resultados antes de passar para a próxima etapa.
- **Documentação:** Mantenha comentários nos scripts para explicar cada parte durante a apresentação.
- **Backup:** Faça backup do banco de dados antes de executar scripts que modificam dados ou estrutura, para evitar perda de informações durante testes.

## Contato para Dúvidas

Caso surjam dúvidas durante a execução dos scripts ou preparação para a apresentação, entre em contato com os monitores responsáveis:

- **Lucas Sena:** lucas.sena@lsbd.ufc.br
- **Lucas Cabral:** lucas.cabral@lsbd.ufc.br

**Nota:** Ao enviar e-mails, coloque ambos os monitores em cópia.

---

**Boa sorte na sua apresentação!**
