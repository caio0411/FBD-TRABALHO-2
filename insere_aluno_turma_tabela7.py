
import psycopg

# Dados de conexão
HOST = "200.129.44.249"
DATABASE = "555025"
USER = "555025"
PASSWORD = "555025"

# Dados a serem inseridos (Tabela 7)
dados_tabela7 = [
    (3, 1),
    (5, 1),
    (4, 1)
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
        for aluno_id, turma_id in dados_tabela7:
            try:
                cur.execute("""
                    INSERT INTO Aluno_Turma (aluno_id, turma_id)
                    VALUES (%s, %s);
                """, (aluno_id, turma_id))
                print(f"Aluno {aluno_id} inserido na turma {turma_id} com sucesso.")
            except Exception as e:
                print(f"Erro ao inserir aluno {aluno_id} na turma {turma_id}: {e}")

# Fecha a conexão
conn.close()
