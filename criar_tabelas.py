import psycopg
from psycopg import sql

# Dados de conexão
conn_info = "host=200.129.44.249 dbname=555025 user=555025 password=555025"

# Abre um cursor para executar comandos

with psycopg.connect(conn_info) as conn:
    with conn.cursor() as cur:
        # Desabilitar restrições temporariamente (opcional)
        # cur.execute("SET session_replication_role = replica;")
            
        # Drop das tabelas se existirem
        tabelas = ["Aluno Turma", "Turma", "Disciplina", "Professor", "Aluno", "Curso"]
        for tabela in tabelas:
                cur.execute(sql.SQL("DROP TABLE IF EXISTS {} CASCADE;").format(sql.Identifier(tabela.replace(" ", "_"))))
            
        # Criação das tabelas
        cur.execute("""
            CREATE TABLE Curso (
                id INT PRIMARY KEY,
                nome VARCHAR(100),
                regime VARCHAR(20),
                duracao INT
            );
        """)

        cur.execute("""
            CREATE TABLE Aluno (
                id INT PRIMARY KEY,
                nome VARCHAR(100),
                curso_id INT REFERENCES Curso(id),
                semestre INT
            );
        """)

        cur.execute("""
            CREATE TABLE Professor (
                id INT PRIMARY KEY,
                nome VARCHAR(100),
                area_especializacao VARCHAR(100),
                contato VARCHAR(100),
                curso_id INT REFERENCES Curso(id)
            );
        """)

        cur.execute("""
            CREATE TABLE Disciplina (
                id INT PRIMARY KEY,
                codigo VARCHAR(10) UNIQUE,
                nome VARCHAR(100),
                area_especializacao VARCHAR(100),
                carga_horaria INT,
                curso_id INT REFERENCES Curso(id)
            );
        """)

        cur.execute("""
            CREATE TABLE Turma (
                id INT PRIMARY KEY,
                codigo VARCHAR(10) UNIQUE,
                disciplina_id INT REFERENCES Disciplina(id),
                semestre VARCHAR(20),
                capacidade_maxima INT,
                estado VARCHAR(20),
                prof_id INT REFERENCES Professor(id)
            );
        """)

        cur.execute("""
            CREATE TABLE Aluno_Turma (
                aluno_id INT REFERENCES Aluno(id),
                turma_id INT REFERENCES Turma(id),
                PRIMARY KEY (aluno_id, turma_id)
            );
        """)

        print("Tabelas criadas com sucesso.")

# Fecha a conexão
conn.close()
