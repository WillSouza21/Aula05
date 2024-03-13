import sqlite3
from modelo import Pessoa, Marca, Veiculo

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa( 
               cpf INTEGER PRIMARY KEY, 
               nome TEXT NOT NULL, 
               nascimento DATE NOT NULL, 
               oculos BOOLEAN NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
               id INTEGER NOT NULL, 
               nome TEXT NOT NULL, 
               sigla CHARACTER(2) 
               NOT NULL, PRIMARY KEY(ID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
               placa CHARACTER(7) NOT NULL,
               ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
               proprietario INTEGER NOT NULL,
               marca INTEGER NOT NULL,
               PRIMARY KEY(placa),
               FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
)''')

#cursor.execute('''ALTER TABLE Veiculo ADD motor REAL''')

pessoa = Pessoa(92345678900,'Pedro', '2000-0131', True)
#inserção com base em querys dinâmicas
comando = '''INSERT INTO Pessoa(cpf, nome, nascimento, oculos) VALUES(?,?,?,?)'''
#cursor.execute(comando,(pessoa.cpf,pessoa.nome,pessoa.nascimento,pessoa.usa_oculos))

#inserir uma lista de Objetos

pessoas =[Pessoa(12345667800,"João","2002-01-31",True),Pessoa(987654321000,'Cynthia', '1995-03-10', False)]

comando_='''INSERT INTO Pessoa(cpf,nome,nascimento,oculos)VALUES(?,?,?,?)'''
cursor.executemany(comando_,[(i.cpf,i.nome,i.nascimento,i.usa_oculos) for i in pessoas])

banco.commit()
cursor.close()
banco.close()