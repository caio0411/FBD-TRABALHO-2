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

try:
    with conn:
        with conn.cursor() as cur:
            # Iniciar transação
            # Atualizar estado da turma
            cur.execute("""
                UPDATE Turma
                SET estado = 'Fechado'
                WHERE codigo = 'CC2024DS1';
            """)

            # Remover matrículas de alunos na turma
            cur.execute("""
                DELETE FROM Aluno_Turma
                WHERE turma_id = (
                    SELECT id FROM Turma WHERE codigo = 'CC2024DS1'
                );
            """)

            print("Transação realizada com sucesso.")

except Exception as e:
    print("Ocorreu um erro durante a transação:", e)
    conn.rollback()

finally:
    # Fecha a conexão
    conn.close()
