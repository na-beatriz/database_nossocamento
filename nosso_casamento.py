#importe das bibliotecas utilizafas
import sqlite3
import csv

#criando database nosso casamento
banco_nossocasamento = sqlite3. connect('Nosso_Casamento.db')


#############################################################################################

#Criação da tabela "Recado para os Noivos"
cursor = banco_nossocasamento.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS recado_noivos(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Nome TEXT NOT NULL,\
               E-mail TEXT NOT NULL,\
               Mensagem TEXT NOT NULL)")

#Define a consulta SQL para inserir dados na tabella "recado para os noivos"
add_recado ="INSERT INTO recadonoivos(Nome, E-mail, Mensagem)VALUES(?, ?, ?)"

#Inserindo dados na database
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, E-mail, Mensagem) VALUES ("Ana Beatriz Almeida", "ana@gmail.com", "recadoA")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, E-mail, Mensagem) VALUES ("André Santos", "andre.santos@gmail.com", "recadoB")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, E-mail, Mensagem) VALUES ("Clissia Carvalho", "clissia.carvalho@gmail.com", "recadoC")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, E-mail, Mensagem) VALUES ("Mari Cristina", "mari_cristina@gmail.com", "recadoD")')
banco_nossocasamento.execute('INSERT INTO recadonoivos(Nome, E-mail, Mensagem) VALUES ("Valéria Araújo", "val_araujo@gmail.com", "recadoE")')
banco_nossocasamento.execute('INSERT INTO recadoNoivos(Nome, E-mail, Mensagem) VALUES ("Jailson Bernandes", "jslsecret@gmail.com", "recadoF")')

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM recadonoivos"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

banco_nossocasamento.commit();
banco_nossocasamento.close();

#############################################################################################

#Criação da tabela "Confirmação de Presença"
cursor = banco_nossocasamento.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS conf_presenca(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Nome TEXT NOT NULL,\
               Convidado NUMBER NOT NULL, \
               Presenca BOOLEAN NOT NULL, \
               E-mail TEXT NOT NULL)")

#Define a consulta SQL para inserir dados na tabella "recado para os noivos"
add_recado ="INSERT INTO conf_presenca(Nome, Convidado, Presenca, E-mail)VALUES(?, ?, ?, ?)"

#Inserindo dados na database

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM conf_presenca"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

banco_nossocasamento.commit();
banco_nossocasamento.close();

#############################################################################################

#Criação da tabela "Lista de Presentes"
cursor = banco_nossocasamento.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS lista_presentes(\
               id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Item TEXT NOT NULL, \
               Preco FLOAT NOT NULL, \
               Nome TEXT NOT NULL,\
               E-mail TEXT NOT NULL)")

#Define a consulta SQL para inserir dados na tabella "recado para os noivos"
add_recado ="INSERT INTO lista_presentes(Item, Preco, Nome, E-mail)VALUES(?, ?, ?, ?)"

#Inserindo dados na database

#define a consulta SQL para selecionar todos os registros da tabela
selecionar_tudo = "SELECT * FROM lista_presentes"

#executa a consulta SQL para obter todas as entradas da tabela .
entradas = cursor.execute(selecionar_tudo).fetchall

banco_nossocasamento.commit();
banco_nossocasamento.close();