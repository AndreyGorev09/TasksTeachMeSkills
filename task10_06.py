with open('File_1.txt', 'w') as my_file_1:
    my_file_1.writelines(['Моя первая строка в "File__1"\n', 'Моя вторая строка в "File__1"\n',
                          'Моя третья строка в "File_1"\n', 'Моя четвертая  строка в "File_1"\n',
                          'Моя пятая строка в "File_1"\n', 'Моя шестая строка в "File_1"\n'])
    my_file_1.close()
with open('File_1.txt') as my_file_1:
    list_str_1 = my_file_1.readlines()
    list_int_str_1 = []
    for line in list_str_1:
        list_int_str_1.append(len(line))
    dict_1 = dict(zip(list_str_1,list_int_str_1))

with open('File_2.txt', 'w') as my_file_2:
    my_file_2.writelines(['Моя первая строка в "File__1"\n', 'Моя вторая строка в "File__1"\n',
                          'Моя третья строка в "File_1"\n', 'Моя десятая строка в "File_1"\n',
                          'Моя одиннадцатая строка в "File_1"\n', 'Моя двенадцатая строка в "File_1"\n'])
    my_file_2.close()
with open('File_2.txt') as my_file_2:
    list_str_2 = my_file_2.readlines()
    list_int_str_2 = []
    for line in list_str_2:
        list_int_str_2.append(len(line))
    dict_2 = dict(zip(list_str_2, list_int_str_2))
x = dict_1.keys()
y = dict_2.keys()
print(x == y)
a =[]
for i in dict_1.keys():
    a.append(i in dict_2.keys())
print(a)
print(a.index(False))