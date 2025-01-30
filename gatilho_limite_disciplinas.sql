-- gatilho_limite_disciplinas.sql

CREATE OR REPLACE FUNCTION limitar_disciplinas()
RETURNS TRIGGER AS $$
DECLARE
    semestre_atual VARCHAR(20);
    disciplinas_contadas INT;
BEGIN
    -- Obter o semestre da turma que está sendo inserida
    SELECT t.semestre INTO semestre_atual
    FROM Turma t
    JOIN Aluno_Turma at ON t.id = at.turma_id
    WHERE at.aluno_id = NEW.aluno_id
    LIMIT 1;

    -- Contar quantas disciplinas o aluno já está matriculado no semestre
    SELECT COUNT(DISTINCT t.disciplina_id) INTO disciplinas_contadas
    FROM Aluno_Turma at
    JOIN Turma t ON at.turma_id = t.id
    WHERE at.aluno_id = NEW.aluno_id
      AND t.semestre = semestre_atual;

    IF disciplinas_contadas >= 4 THEN
        RAISE EXCEPTION 'Aluno já está matriculado em 4 disciplinas neste semestre.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar o gatilho na tabela Aluno_Turma
DROP TRIGGER IF EXISTS gatilho_limitar_disciplinas ON Aluno_Turma;

CREATE TRIGGER gatilho_limitar_disciplinas
BEFORE INSERT ON Aluno_Turma
FOR EACH ROW
EXECUTE FUNCTION limitar_disciplinas();
