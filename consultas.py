import psycopg

# Dados de conexão
HOST = "200.129.44.249"
DATABASE = "555025"
USER = "555025"
PASSWORD = "555025"

# Conexão com o banco de dados
conn = psycopg.connect(
    host=HOST,
    dbname=DATABASE,
    user=USER,
    password=PASSWORD
)

with conn:
    with conn.cursor() as cur:
        # 1. Retornar todas as turmas e a quantidade de alunos participantes de cada turma
        print("1. Turmas e quantidade de alunos participantes:")
        cur.execute("""
            SELECT t.codigo, COUNT(at.aluno_id) AS quantidade_alunos
            FROM Turma t
            LEFT JOIN Aluno_Turma at ON t.id = at.turma_id
            GROUP BY t.codigo
            ORDER BY t.codigo;
        """)
        turmas = cur.fetchall()
        for turma in turmas:
            print(f"Turma: {turma[0]}, Quantidade de Alunos: {turma[1]}")
        print("\n")

        # 2. Retornar os alunos matriculados na disciplina de “Fundamentos de Bancos de Dados”
        print("2. Alunos matriculados na disciplina 'Fundamentos de Bancos de Dados':")
        cur.execute("""
            SELECT a.id, a.nome
            FROM Aluno a
            JOIN Aluno_Turma at ON a.id = at.aluno_id
            JOIN Turma t ON at.turma_id = t.id
            JOIN Disciplina d ON t.disciplina_id = d.id
            WHERE d.nome = 'Fundamentos de Bancos de Dados';
        """)
        alunos = cur.fetchall()
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}")
        print("\n")

        # 3. Retornar a quantidade de professores do curso de “Ciências da Computação”
        print("3. Quantidade de professores do curso 'Ciências da Computação':")
        cur.execute("""
            SELECT COUNT(*) 
            FROM Professor p
            JOIN Curso c ON p.curso_id = c.id
            WHERE c.nome = 'Ciências da Computação';
        """)
        quantidade_professores = cur.fetchone()[0]
        print(f"Quantidade de Professores: {quantidade_professores}")

# Fecha a conexão
conn.close()
