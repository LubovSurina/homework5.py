immutable_var=(1, 'f', 5, True, 'V')
print(immutable_var)
#immutable_var[2]=8
#print(immutable_var)#мы не можем заменить элемент в кортеже, так как это неизменяемая структура
mutable_list=[5, 8, 'H', 'r', False]
print(mutable_list)
mutable_list[2]='Book'
print(mutable_list)