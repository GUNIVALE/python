def cria_lista():
    # variavel "numeros" vai para a stack
    # a lista {1,2,3} vai para o Heap
    numeros = [1, 2, 3]
    return numeros

resultados = cria_lista()
# a função acabou, mas a lista
# aomda existe mp Heap
print(resultados) # {1, 2, 3}