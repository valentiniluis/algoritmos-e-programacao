# 10 - Crie um programa que gere automaticamente uma lista de 100 números aleatórios. Em seguida, percorra a lista
# identificando quais valores estão duplicados. Insira os elementos duplicados em outra lista e imprima-a ao final
# do programa.

import random
duplicados = list()

lista = list()
for i in range(100):
  lista.append(random.randint(0, 1000))

for i in lista:
  if i in duplicados:
    continue
  elif lista.count(i) >= 2:
    duplicados.append(i)

print(duplicados)