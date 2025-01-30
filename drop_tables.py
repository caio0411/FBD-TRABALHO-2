import psycopg
conn_info = "host=200.129.44.249 dbname=555025 user=555025 password=555025"

try:
    with psycopg.connect(conn_info) as conn:
        with conn.cursor() as cur:
            # Buscar todas as tabelas do schema público
            cur.execute("""
                SELECT tablename FROM pg_tables
                WHERE schemaname = 'public';
            """)
            tabelas = cur.fetchall()

            for tabela in tabelas:
                cur.execute(f'DROP TABLE IF EXISTS "{tabela[0]}" CASCADE;')
                print(f"Tabela {tabela[0]} apagada.")

            conn.commit()
except Exception as e:
    print(f"Erro ao apagar tabelas: {e}")