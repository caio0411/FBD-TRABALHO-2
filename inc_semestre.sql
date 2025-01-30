-- inc_semestre.sql

CREATE OR REPLACE PROCEDURE inc_semestre(IN semestre_atual INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Aluno
    SET semestre = semestre + 1
    WHERE semestre = semestre_atual;
END;
$$;
