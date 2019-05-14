def filaTop():
    filanome = [] #fila dos nomes
    filapedido = [] #fila dos pedidos
    filapreco = [] #fila dos precos

    ## para receber os nomes e pedidos por input e adicionar a cada lista
    for x in range(0,7):
        nome = input("insira o nome: ")
        pedido = input("insira o pedido: ")
        pdd = pedido.lower() #transforma em minuscula
        preco = ""
        
        ##encontrar o preco correspondente
        if pdd == "salgado":
            preco = 4
        elif pdd == "refrigerante":
            preco = 4.50
        elif pdd == "suco":
            preco = 5
        elif pdd == "sorvete":
            preco = 6
        elif pdd == "cafe":
            preco = 4
        elif pdd == "capuccino":
            preco = 6
        elif pdd == "bolo":
            preco = 4.50
        elif pdd == "dadinho":
            preco = 0.50

        #vai pra lista correspondente
        filanome.append(nome) #nome vai para a fila dos nomes
        filapedido.append(pdd) #pedido vai para a fila dos pedidos
        filapreco.append(preco) #para encontrar o preco correspondente

    #soma dos precos
    soma = 0
    for i in filapreco:
        soma = soma + i #acumula a soma
        
    #para imprimir os nomes e pedidos igual pede o exercicio
    y = 0
    while y < 7:
        print(filanome[y],"-", filapedido[y],"-", filapreco[y]) #imprime cada indice das listas
        y = y + 1
        
    print("O valor final em caixa é {}".format(soma)) #imprime o valor final em caixa

filaTop()
