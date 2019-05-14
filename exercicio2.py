def fila():
    filanome = [] #fila dos nomes
    filapedido = [] #fila dos pedidos

    ## para receber os nomes e pedidos por input e adicionar a cada lista
    for x in range(0,7):
        nome = input("insira o nome: ")
        pedido = input("insira o pedido: ")
        filanome.append(nome) #nome vai para a fila dos nomes
        filapedido.append(pedido) #pedido vai para a fila dos pedidos

    #para imprimir os nomes e pedidos igual pede o exercicio
    y = 0
    while y < 7:
        print(filanome[y],"-", filapedido[y]) #imprime cada indice das listas
        y = y + 1
    
    
fila() #chamada da função
