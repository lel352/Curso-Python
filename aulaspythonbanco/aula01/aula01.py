import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#               'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#               'nome TEXT,'
#               'peso REAL'
#               ')')


#cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Peter Paker", 80.5)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#               {'nome': 'João', 'peso': 25})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#               {'id': None, 'nome': 'Daniel', 'peso': 113})
# conexao.commit()


# cursor.execute('UPDATE clientes set nome = :nome where id=:id',
#               {'nome': 'Joana', 'id': 2})
# conexao.commit()

# cursor.execute('DELETE FROM clientes WHERE id= ?', '2')
# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():  # cursor.fetchall() # buscando todos os valores da tabela clientes
    print(linha)  # cada linha tem um tupla com as colunas
    identificador, nome, peso = linha

    print(identificador, nome, peso)

print('*'*25)

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

for linha in cursor.fetchall():  # cursor.fetchall() # buscando todos os valores da tabela clientes
    print(linha)  # cada linha tem um tupla com as colunas


cursor.close()
conexao.close()