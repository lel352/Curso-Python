import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) values (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE or IGNORE agenda SET nome = ?, telefone = ? where id = ?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda  where id = ?'
        self.cursor.execute(consulta, (id,)) # Colocar a virgula para ser uma tupla.
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda where nome like ?'
        self.cursor.execute(consulta, (f'%{valor}%', ))
        for linha in self.cursor.fetchall():
            print(linha)


    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Peter', '123456')
    # agenda.inserir('Steve', '333333')
    # agenda.inserir('Tony', '12342425')
    # agenda.inserir('Clark', '1222236')
    agenda.inserir('Bruce', '989899')
    # agenda.inserir('Oliver', '93424234')
    # agenda.editar('Pinga', '11111111', 6)
    # agenda.excluir(8)
    agenda.inserir('Peter Parker', '123424377777777777777777777777777756342')
    agenda.inserir('Steve Roger', '33234242343')
    agenda.inserir('Bruce Barner', '989234234234899')
    agenda.inserir('Brucer Vai', '98923442234899')
    agenda.inserir('Steve Vai', '989234234234899')

    agenda.buscar('Bruce')
    # agenda.listar()

