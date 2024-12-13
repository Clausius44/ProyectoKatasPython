"""33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""

vec1 = [1, 2, 3, 4]
vec2 = [10, 20]

sumaTotal = lambda list1, list2: sum(list1) + sum(list2)

print(sumaTotal(vec1, vec2))