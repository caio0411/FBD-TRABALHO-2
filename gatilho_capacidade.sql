-- gatilho_capacidade.sql

CREATE OR REPLACE FUNCTION verificar_capacidade()
RETURNS TRIGGER AS $$
DECLARE
    capacidade INT;
    matriculados INT;
BEGIN
    -- Obter a capacidade máxima da turma
    SELECT capacidade_maxima INTO capacidade
    FROM Turma
    WHERE id = NEW.turma_id;

    -- Contar o número de alunos atualmente matriculados
    SELECT COUNT(*) INTO matriculados
    FROM Aluno_Turma
    WHERE turma_id = NEW.turma_id;

    IF matriculados >= capacidade THEN
        RAISE EXCEPTION 'Capacidade máxima da turma atingida.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar o gatilho na tabela Aluno_Turma
DROP TRIGGER IF EXISTS gatilho_verificar_capacidade ON Aluno_Turma;

CREATE TRIGGER gatilho_verificar_capacidade
BEFORE INSERT ON Aluno_Turma
FOR EACH ROW
EXECUTE FUNCTION verificar_capacidade();
