import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Thiago2004',
    database='lista'
)

cursor = conexao.cursor()

print("O que deseja?")
print('-------------')  
print("Fazer comanda - (1)")
print('-------------')  
print("Adiconar produto - (2)")
print('-------------')  
print("Ver lista de produtos - (3)")
print('-------------')
print("Atualizar produto - (4)")
print('-------------')
print("Excluir produto - (5)")
print('-------------')

decisao = int (input('1, 2, 3, 4 ou 5: '))

total = 0

x = 0

if decisao == 1 :
    while (x == 0):
        valor = float (input ('Valor: '))
        total = total + valor
        print ('Deseja continuar? (0) sim, (1) não: ')
        y = int (input('0 ou 1: '))
        if y == 1:
            x = x + 1
            
    print('-------------')  
    print(total)

elif decisao == 2 :
    nome = str (input('nome a ser inserido: '))
    comando = f'INSERT INTO PESSOAS (nome) VALUES ("{nome}")'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Inserido com sucesso!')
        
elif decisao == 3 :
    comando = f'SELECT * FROM pessoas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('-------------')
    print(resultado)

elif decisao == 4 :
    print('-------------')
    id_vr = (input('digite o id do item a ser modificado: '))
    nome_mod = (input('Nome atualizado: '))
    comando = f'UPDATE pessoas SET nome = "{nome_mod}" WHERE id = {id_vr}'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Atualizado com sucesso!')

elif decisao == 5 :
    print('-------------')
    id_del = (input('digite o id do item a ser excluído: '))
    comando = f'DELETE FROM pessoas WHERE id = {id_del}'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Excluído com sucesso!')


cursor.close()
conexao.close()