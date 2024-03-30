
def foo(nomber, flag, list = []):
    if nomber == 0:
        return list, sum(list)
    if flag == True and nomber % 2 == 0:
        list.append(nomber % 10)
    if flag == False and nomber % 2 == 1:
        list.insert(0, nomber % 10)

    nomber = nomber // 10
    return foo(nomber, flag, list)

list =[]

a = foo(785963121, False, list)
print(a)