def write_list_txt():
    str_line_1 = input('Введите строку_1: ')
    str_line_2 = input('Введите строку_2: ')
    str_line_3 = input('Введите строку_3: ')
    str_line_4 = input('Введите строку_4: ')
    str_line_5 = input('Введите строку_5: ')
    str_line_6 = input('Введите строку_6: ')
    with open('Strings.txt', 'w') as my_file:
        my_file.writelines([f'{str_line_1}\n{str_line_2}\n{str_line_3}\n{str_line_4}\n{str_line_5}\n{str_line_6}\n'])

print(write_list_txt())


with open("Strings.txt") as my_file, open("Strings.txt_1", "w") as my_file_1, open("Strings.txt_2", "w") as my_file_2:
    count=1
    for list in my_file.readlines():
        if count%2==0:
            my_file_1.write(list)
        else:
            my_file_2.write(list)
        count+=1

with open("Strings.txt_1") as my_file_1:
    print(my_file_1.readlines())

with open("Strings.txt_2") as my_file_2:
    print(my_file_2.readlines())