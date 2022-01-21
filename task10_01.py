my_file = open('File.txt', 'w')
my_file.writelines(['Srting num 1\n', 'Srting num 2\n', 'Srting num 3\n', 'Srting num 4\n', 'Srting num 5\n',
                    'Srting num 6\n'])
my_file.close()


my_file = open('File.txt')
def str_file(x = None, y = None):
    list_string = []
    while True:
        for line in my_file:
            list_string.append(line)
        return list_string[x:y]
print(str_file(0, 2))