def new_write_txt():
    str_line_7 = input('Введите строку_7: ')
    str_line_8 = input('Введите строку_8: ')
    str_line_9 = input('Введите строку_9: ')
    with open('Strings.txt', 'a') as my_file:
        my_file.writelines([f'{str_line_7}\n{str_line_8}\n{str_line_9}\n'])
        my_file.close()
    with open('Strings.txt') as my_file:
        for list in my_file:
            print(list)
    return my_file.close()
print(new_write_txt())