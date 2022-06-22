import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Thiago2004',
    database='lista'
)

cursor = conexao.cursor()

#inserir
""" nome = str (input('nome a ser inserido: '))
comando = f'INSERT INTO PESSOAS (nome) VALUES ("{nome}")'
cursor.execute(comando)
conexao.commit() """

#ver dados
""" comando = f'SELECT * FROM pessoas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado) """

#atualizar dados 
""" id_vr = (input('digite o id do item a ser modificado: '))
nome_mod = (input('Nome atualizado: '))
comando = f'UPDATE pessoas SET nome = "{nome_mod}" WHERE id = {id_vr}'
cursor.execute(comando)
conexao.commit() """

#excluir dados
id_del = (input('digite o id do item a ser excluído: '))
comando = f'DELETE FROM pessoas WHERE id = {id_del}'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()