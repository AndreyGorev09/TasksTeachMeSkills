def revers_int():
    with open('File_1.txt', 'w') as my_file_1:
        my_file_1.writelines(['Моя первая строка, в ней есть значение 0\n', 'Моя втовая строка вней есть значение 1\n'])
        my_file_1.close()
    with open('File_1.txt') as my_file_1:
        print(my_file_1.readlines())
        my_file_1.close()

    with open('File_1.txt') as my_file_2:
        for line in my_file_2:
            while True:
                if '0' in line:
                    a = line.replace('0', '1')
                    break
                else:
                    b = line.replace('1', '0')
                    break
    with open('File_2.txt', 'w') as my_file_2:
        my_file_2.writelines([f'{a}{b}'])
    my_file_2.close()
    with open('File_2.txt') as my_file_2:
        return my_file_2.readlines()
print(revers_int())
