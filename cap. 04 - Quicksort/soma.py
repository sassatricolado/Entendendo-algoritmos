lista = [1, 3, 5, 7, 9]

def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

print(soma(lista))

def contador_de_item(lista):
    if lista == []:
        return 0
    return 1 + contador_de_item(lista[1:])

print(contador_de_item(lista))

def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maximo(lista))