def contagem_regressiva(n):
    print(n)
    if n <= 1:
        return
    contagem_regressiva(n - 1)

contagem_regressiva(10)