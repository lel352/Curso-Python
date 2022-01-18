import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()

with conecta() as conexao: # gerenciador de contexto da conexão
    with conexao.cursor() as cursor: # gerenciador de contexto do cursor
        # Insere um registro
        # sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        # cursor.execute(sql, ('Peter', 'Parker', 25, 90))
        # Insere vários registro
        # dados = [
        #    ('Mary', 'Jane', '24', 65),
        #    ('Ben', 'Relly', '25', 90),
        #    ('Gwen', 'Stacy', '23', 60),
        # ]
        #cursor.executemany(sql, dados)

        # sql = 'DELETE FROM clientes WHERE id = %s'
        # cursor.execute(sql, (5, ))
        # sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        # cursor.execute(sql, (7, 8, 9))
        # sql = 'DELETE FROM clientes WHERE id BETWEEN %s and %s'
        # cursor.execute(sql, (10, 12))

        # sql = 'UPDATE clientes SET nome = %s WHERE ID = %s'
        # cursor.execute(sql, ('Xavier', 1))

        conexao.commit()


with conecta() as conexao:  # gerenciador de contexto da conexão
    with conexao.cursor() as cursor:  # gerenciador de contexto do cursor
        print('*' * 25)
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 20')
        resultado = cursor.fetchall()  # All - todos os registro, many - pega uma quantidade de resgistro, one - pega soemnte 1

        for linha in resultado:
            print(linha)
            # print(linha['nome'])
            # print(linha['sobrenome'])

        print('*' * 25)

        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 20')
        resultado = cursor.fetchall()
