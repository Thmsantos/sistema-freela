import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Thiago2004',
    database='produtos'
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
print("Atualizar nome do produto - (4)")
print('-------------')
print("Atualizar nome do produto - (5)")
print('-------------')
print("Excluir produto - (6)")
print('-------------')

decisao = int (input('1, 2, 3, 4, 5 ou 6: '))

total = 0

x = 0

if decisao == 1 :
    while (x == 0):
        valor = float (input ('Valor: '))
        total = total + valor
        print ('Deseja continuar? (0) sim, (1) não: ')
        y = float (input('0 ou 1: '))
        if y == 1:
            x = x + 1
            
    print('-------------')  
    print(total)

elif decisao == 2 :
    nome = str (input('Nome do produto a ser inserido: '))
    valor = float (input('Valor do produto a ser inserido: '))
    comando = f'INSERT INTO ITEMS (nome_produto, valor) VALUES ("{nome}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Inserido com sucesso!')
        
elif decisao == 3 :
    comando = f'SELECT * FROM items'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('-------------')
    print(resultado)

elif decisao == 4 :
    print('-------------')
    nome_prod = str (input('digite o nome do produto a ser modificado: '))
    nome_mod = str (input('Novo nome do produto: '))
    comando = f'UPDATE items SET nome_produto = "{nome_mod}" WHERE nome_produto = "{nome_prod}"'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Atualizado com sucesso!')

elif decisao == 5 :
    print('-------------')
    nome_prod = str (input('digite o nome do produto a ser modificado: '))
    valor_mod = float (input('Novo valor: '))
    comando = f'UPDATE items SET valor = {valor_mod} WHERE nome_produto = "{nome_prod}"'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Atualizado com sucesso!')

elif decisao == 6 :
    print('-------------')
    nome_del = (input('digite o nome do item a ser excluído: '))
    comando = f'DELETE FROM pessoas WHERE id = {nome_del}'
    cursor.execute(comando)
    conexao.commit()
    print('-------------')  
    print('Excluído com sucesso!')

cursor.close()
conexao.close()