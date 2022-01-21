list_world = ['hello', 'world', 'string', 'tuple', 'int']
new_list = list(list_world[::-1])
new_x = []
for x in new_list:
    new_x.append(x[::-1])
print(new_x)