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
        try:
            # Chamar o procedimento armazenado
            cur.execute("CALL inc_semestre(%s);", (1,))
            print("Procedimento armazenado chamado com sucesso.")
        except Exception as e:
            print("Erro ao chamar o procedimento armazenado:", e)

# Fecha a conexão
conn.close()
