immutable_var = (47, "Lee", False)
print('Immutable tuple:',immutable_var)
#immutable_var [0] = 7 - Кортеж не поддерживает изменения по элементам
mutable_list = [47,"Lee", False]
mutable_list[0] = 7
print('Mutable list:',mutable_list)