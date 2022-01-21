with open('File.txt', 'w') as my_file:
    my_file.writelines(['Строка с четным количеством символов__1\n', 'Строка с четным количеством символов__2\n'
                        'Строка с НЕЧЕТНЫМ количеством символов_1\n', 'Строка с НЕЧЕТНЫМ количеством символов_2\n'
                        ])
my_file.close()

with open('File.txt') as my_file:
    new_list_even = []
    new_list_odd = []
    for line in my_file:
        for i in line:
            if len(line) % 2 == 0:
                even = line
                new_list_even.append(even)
                a = new_list_even
                break
            else:
                odd = line
                new_list_odd.append(odd)
                b = new_list_odd
                break

with open('File_1.txt', 'w') as my_file_1:
    my_file_1.writelines(a)
    my_file_1.close()
with open('File_1.txt') as my_file_1:
    print(my_file_1.readlines())

with open('File_2.txt', 'w') as my_file_2:
    my_file_2.writelines(b)
    my_file_2.close()
with open('File_2.txt') as my_file_2:
    print(my_file_2.readlines())