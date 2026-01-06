def calcular_xp(n1, n2, tabela):
    total = 0
    for n in range(n1, n2):
        total += tabela.get(str(n), 0)
    return total
