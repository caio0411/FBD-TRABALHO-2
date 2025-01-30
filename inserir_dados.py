import psycopg

# Dados de conexão
HOST = "200.129.44.249"
DATABASE = "555025"
USER = "555025"
PASSWORD = "555025"

# Dados para inserção
dados_curso = [
    (1, "Ciências da Computação", "Semestral", 8),
    (2, "Engenharia de Software", "Anual", 10),
    (3, "Sistemas de Informação", "Semestral", 8)
]

dados_aluno = [
    (1, "João Silva", 1, 1),
    (2, "Maria Costa", 1, 1),
    (3, "Ana Souza", 3, 5),
    (4, "Pedro Almeida", 2, 3),
    (5, "Lucas Santos", 2, 3)
]

dados_professor = [
    (1, "Maria Oliveira", "Banco de Dados", "maria@ufc.br", 1),
    (2, "João Pereira", "Redes de Computadores", "joao@ufc.br", 2),
    (3, "Ana Silva", "Inteligência Artificial", "ana@ufc.br", 3),
    (4, "Paulo Santos", "Engenharia de Software", "paulo@ufc.br", 2),
    (5, "Carla Mendes", "Redes de Computadores", "carla@ufc.br", 1)
]

dados_disciplina = [
    (1, "BD001", "Fundamentos de Bancos de Dados", "Banco de Dados", 60, 1),
    (2, "IA002", "Inteligência Computacional Aplicada", "Inteligência Artificial", 80, 3),
    (3, "RS003", "Segurança da Informação", "Redes de Computadores", 40, 2),
    (4, "BD004", "Introdução a Ciência de Dados", "Banco de Dados", 60, 1),
    (5, "ES005", "Qualidade de Software", "Engenharia de Software", 50, 2)
]

dados_turma = [
    (1, "CC2024BD1", 1, "2024.2", 4, "Aberta", 1),
    (2, "CC2024IA1", 2, "2024.2", 4, "Aberta", 3),
    (3, "CC2024RS1", 3, "2024.2", 8, "Aberta", 2),
    (4, "CC2024DS1", 4, "2024.2", 4, "Aberta", 1),
    (5, "CC2024ES1", 5, "2024.2", 8, "Aberta", 4)
]

dados_aluno_turma = [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (1, 5),
    (2, 4),
    (3, 5),
    (4, 2),
    (5, 3)
]

# Conexão com o banco de dados
conn = psycopg.connect(
    host=HOST,
    dbname=DATABASE,
    user=USER,
    password=PASSWORD
)

with conn:
    with conn.cursor() as cur:
        # Inserção na tabela Curso
        cur.executemany("""
            INSERT INTO Curso (id, nome, regime, duracao)
            VALUES (%s, %s, %s, %s);
        """, dados_curso)

        # Inserção na tabela Aluno
        cur.executemany("""
            INSERT INTO Aluno (id, nome, curso_id, semestre)
            VALUES (%s, %s, %s, %s);
        """, dados_aluno)

        # Inserção na tabela Professor
        cur.executemany("""
            INSERT INTO Professor (id, nome, area_especializacao, contato, curso_id)
            VALUES (%s, %s, %s, %s, %s);
        """, dados_professor)

        # Inserção na tabela Disciplina
        cur.executemany("""
            INSERT INTO Disciplina (id, codigo, nome, area_especializacao, carga_horaria, curso_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, dados_disciplina)

        # Inserção na tabela Turma
        cur.executemany("""
            INSERT INTO Turma (id, codigo, disciplina_id, semestre, capacidade_maxima, estado, prof_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, dados_turma)

        # Inserção na tabela Aluno_Turma
        cur.executemany("""
            INSERT INTO Aluno_Turma (aluno_id, turma_id)
            VALUES (%s, %s);
        """, dados_aluno_turma)

        print("Dados inseridos com sucesso.")

# Fecha a conexão
conn.close()
