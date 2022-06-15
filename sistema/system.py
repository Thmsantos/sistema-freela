print("O que deseja?")
print('-------------')  
print("Controle de estoque(1)")
print('-------------')  
print("Comando do cliente(2)")
print('-------------')  
print("Lista de produtos(3)")
print('-------------')

decisao = int (input('1, 2 ou 3: '))

total = 0

x = 0

produtos = [
            'Cookie de Morango',
            'Suco de Uva',
            'Cookie de brigadeiro',
            'Coca-Cola',
            'Cookie tradicional'
            ]

if decisao == 1 :
    print('controle de estoque')

elif decisao == 2 :
    while (x == 0):
        valor = float (input ('Valor: '))
        total = total + valor
        print ('Deseja continuar? (0) sim, (1) não: ')
        y = int (input('0 ou 1: '))
        if y == 1:
            x = x + 1
            
    print('-------------')  
    print(total)
        
elif decisao == 3 :
    print('-------------')  
    print (produtos)




