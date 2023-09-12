conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format (conjunto_uniao))

conjunto_intersec = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_intersec))

conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença: {}'.format (conjunto_diferenca))

#Diferença simétrica

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}


conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B {} '.format (conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A {}'.format (conjunto_superset))


lista = ['gato','cachorro', 'gato', 'elefante', 'lobo', 'arara']
conjunto_animais = set(lista)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)

conjunto = {1, 2, 3, 4, 4, 5}
conjunto.add(5)
conjunto.discard(2)
print(conjunto) 
