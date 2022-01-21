def write_list_txt():
    str_line_1 = input('Введите строку_1: ')
    str_line_2 = input('Введите строку_2: ')
    str_line_3 = input('Введите строку_3: ')
    str_line_4 = input('Введите строку_4: ')
    str_line_5 = input('Введите строку_5: ')
    str_line_6 = input('Введите строку_6: ')
    with open('Strings.txt', 'w') as my_file:
        my_file.writelines([f'{str_line_1}\n{str_line_2}\n{str_line_3}\n{str_line_4}\n{str_line_5}\n{str_line_6}\n'])

    with open('Strings.txt') as my_file:
        for list in my_file:
            print(list)
    return my_file.close()
print(write_list_txt())