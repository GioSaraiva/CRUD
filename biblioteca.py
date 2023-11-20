import mysql.connector

def criar(conexao, entrada, at1, at2, at3, at4):
    cursor = conexao.cursor()

    if entrada == 'f':
        comando_sql = f"""INSERT INTO funcionarios (nome, salario, idade) VALUES ('{at1}', {at2}, '{at3}')"""
        cursor.execute(comando_sql)
        conexao.commit()

    if entrada == 'c':
        comando_sql = f"""INSERT INTO clientes (nome, idade, endereco, telefone) VALUES ('{at1}', '{at2}', '{at3}',{at4})"""
        cursor.execute(comando_sql)
        conexao.commit()

    if entrada == 'm':
        comando_sql = f"""INSERT INTO materiais (nome, validade, quantidade) VALUES ('{at1}', '{at2}', {at3})"""
        cursor.execute(comando_sql)
        conexao.commit()

    if entrada == 's':
        comando_sql = f"""INSERT INTO serviços (nome, tempo, valor) VALUES ('{at1}', '{at2}', '{at3}')"""
        cursor.execute(comando_sql)
        conexao.commit()

def ler(conexao, leia):
    cursor = conexao.cursor()
    cursor.execute(f'select * from {leia}')
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

def deletar(conexao,tabela, id):
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE id_{tabela} = {id}")
    conexao.commit()

def atualizar(conexao, tabela, id, coluna, novo_valor):
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE {tabela} SET {coluna} = %s WHERE id_{tabela} = %s", (novo_valor, id))
    conexao.commit()