import sqlite3
banco = sqlite3.connect('database.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE cliente(nome text, idade integer, sexo text)")
cursor.execute("INSERT INTO cliente VALUES('Will',19,'m'), ('pedro',20,'m')")
banco.commit()
cursor.close()
banco.close()

