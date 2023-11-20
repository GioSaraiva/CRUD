import mysql.connector
from biblioteca import*

conexao = mysql.connector.connect(host="localhost", user="root", password="302302", database="salao")

entrada = input(f'Aperte f-funcionarios / c-clientes / m-materiais / s-serviços')

if entrada == 'f':
    at1 = str(input('Digite o nome do funcionario: '))
    at2 = float(input('Digite o salário do funcionario: '))
    at3 = str(input('Digite a data de nascimento:    EX.:(**/**/****)'))
    at4 = '-------------------------------------------------------------'
    criar(conexao, entrada, at1, at2, at3, at4)
    ler(conexao,'funcionarios')
    deletar(conexao, tabela)

elif entrada == 'c':
    at1 = str(input('Digite o nome do cliente: '))
    at2 = str(input('Digite a data de nascimento do cliente: EX.:(**/**/****) '))
    at3 = str(input('Digite o endereço do cliente: '))
    at4 = int(input('Digite o telefone do cliente: '))
    criar(conexao, entrada, at1, at2, at3, at4)
    ler(conexao, 'clientes')

if entrada == 'm':
    at1 = str(input('Digite o nome do material: '))
    at2 = str(input('Digite a data de validade: EX.:(**/**/****) '))
    at3 = int(input('Digite a quantidade: '))
    at4 = '---------------------------------------------------------------'
    criar(conexao, entrada, at1, at2, at3, at4)
    ler(conexao, 'materiais')

if entrada == 's':
    at1 = str(input('Digite o nome do serviço: '))
    at2 = str(input('Digite o tempo do serviço: EX.:(1h30) '))
    at3 = int(input('Digite o valor do serivço:'))
    at4 = '---------------------------------------------------------------'
    criar(conexao, entrada, at1, at2, at3, at4)
    ler(conexao, 'serviços')

