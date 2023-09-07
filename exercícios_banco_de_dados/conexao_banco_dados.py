'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

3. Consultas Básicas 
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
d) Contar o número total de alunos na tabela

4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.
b) Remova um aluno pelo seu ID.

5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:

a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 1000.

7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.

8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

'''


import sqlite3

conexao_banco_dados = sqlite3.connect('banco_dados')
cursor = conexao_banco_dados.cursor()



#Questão 01
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')



#Questão 02
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Maria", 18, "Analise e Desenvolvimento de Sistema")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Luiz", 25, "Sistema de Informação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ana", 32, "Engenharia da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Augusto", 50, "Design")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Fernanda", 22, "Redes de Computadores")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Pedro", 31, "Ciência da Computação")')



#Questão 03
#Letra A:
informações = cursor.execute('SELECT * FROM alunos')

#Letra B:
informações = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')

#Letra C:
informações = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia da Computação" ORDER BY nome')

#Letra D:
informações = cursor.execute('SELECT COUNT(*) FROM alunos')



#Questão 04
#Letra A: Atualização
informações = cursor.execute('UPDATE alunos SET idade = 29 WHERE nome = "Augusto"')

#Letra B: Remoção
informações = cursor.execute('DELETE FROM alunos WHERE id=4')

for alunos in informações:
    print(f'{alunos}\n')



#Questão 05
#Criação da Tabela
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

#Inserindo Dados
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Maria", 25, 2000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "João", 18, 5000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Roberta", 35, 850)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Pedro", 38, 1500)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Mariana", 31, 12000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Júnior", 22, 500)')



#Questão 06
#Letra A:
informações = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')

#Letra B:
informações = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

#Letra C:
informações = cursor.execute('SELECT nome, MAX(saldo) FROM clientes')

#Letra D:
informações = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')



#Questão 07
#Letra A: Atualização
informações = cursor.execute('UPDATE clientes SET saldo = 3000 WHERE nome = "Júnior"')

#Letra B: Remoção
informações = cursor.execute('DELETE FROM clientes WHERE id = 3')

for clientes in informações:
    print(f'{clientes}\n')



#Questão 08
#Criação da Tabela
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor float, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id));')

#Inserindo Dados
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 2, "Ar Condicionado", 3500)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 5, "Geladeira", 4300)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 3, "Fogão", 1900)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 6, "Televisão", 7000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 1, "Celular", 2500)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (6, 4, "Liquidificador", 550)')

#Consulta de dados
informações = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')

for compras in informações:
    print(f'{compras}\n')

conexao_banco_dados.commit()
conexao_banco_dados.close


