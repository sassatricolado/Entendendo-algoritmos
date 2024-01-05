import math

def pesquisa_binaria(lista, item):
   inicio = 0
   fim = len(lista) - 1
   while inicio <= fim:
      meio = math.ceil((inicio + fim) / 2)
      chute = lista[meio]
      if chute == item:
         return meio
      if chute > item:
         fim = meio - 1
      else:
         inicio = meio + 1
   return None

minha_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

print(pesquisa_binaria(minha_lista, 13))