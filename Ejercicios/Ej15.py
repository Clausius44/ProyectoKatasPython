"""15. Crea una función lambda que sume 3 a cada número de una lista dada."""

listNum = [2, 5,  4, 2, 5, 4]
new_listNum_gener = lambda x: x+3
new_list = list(map(new_listNum_gener, listNum))
print(new_list)