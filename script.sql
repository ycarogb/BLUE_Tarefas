CREATE TABLE public.segunda (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE public.terca (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE public.quarta (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE public.quinta (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE public.sexta (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE public.sabado (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE public.domingo (
	tarefa varchar NOT NULL,
	dtagendamento date NULL,
	observacao varchar NULL,
	idtarefa SERIAL PRIMARY KEY
);

CREATE TABLE anotacoes(
	id SERIAL PRIMARY KEY,
	anotacao VARCHAR(255) NOT NULL
);

INSERT INTO segunda (tarefa , observacao, dtagendamento) 
VALUES('atividade 1', 'bla', '05/07/2021');

INSERT INTO segunda (tarefa , observacao, dtagendamento) 
VALUES('atividade 2', 'bla', '05/07/2021');

INSERT INTO terca (tarefa , observacao, dtagendamento) 
VALUES('Ativiade 1', 'bla', '06/07/2021');

INSERT INTO terca (tarefa , observacao, dtagendamento) 
VALUES('Atividade 2', 'bla', '06/07/2021');

INSERT INTO quarta (tarefa , observacao, dtagendamento) 
VALUES('Ativiade 1', 'bla', '06/07/2021');

INSERT INTO quarta (tarefa , observacao, dtagendamento) 
VALUES('Atividade 2', 'bla', '06/07/2021');

INSERT INTO quinta (tarefa , observacao, dtagendamento) 
VALUES('Ativiade 1', 'bla', '06/07/2021');

INSERT INTO quinta (tarefa , observacao, dtagendamento) 
VALUES('Atividade 2', 'bla', '06/07/2021');

INSERT INTO sexta (tarefa , observacao, dtagendamento) 
VALUES('Ativiade 1', 'bla', '06/07/2021');

INSERT INTO sexta (tarefa , observacao, dtagendamento) 
VALUES('Atividade 2', 'bla', '06/07/2021');
INSERT INTO sabado (tarefa , observacao, dtagendamento) 
VALUES('Ativiade 1', 'bla', '06/07/2021');

INSERT INTO sabado (tarefa , observacao, dtagendamento) 
VALUES('Atividade 2', 'bla', '06/07/2021');

INSERT INTO domingo (tarefa , observacao, dtagendamento) 
VALUES('Ativiade 1', 'bla', '06/07/2021');

INSERT INTO domingo (tarefa , observacao, dtagendamento) 
VALUES('Atividade 2', 'bla', '06/07/2021');


INSERT INTO anotacoes (anotacao) 
VALUES('Aplicar estilos');

INSERT INTO anotacoes (anotacao) 
VALUES('Teste1');

INSERT INTO anotacoes (anotacao) 
VALUES('Teste2');