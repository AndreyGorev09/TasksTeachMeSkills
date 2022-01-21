import random
import json

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(random.randint(1, 10))

with open('File.txt_1', 'w') as my_file_1:
    my_file_1.write(json.dumps(matrix))
    my_file_1.close()

with open('File.txt_1') as my_file_1:
    print(json.load(my_file_1))

index_i = 0
for i in matrix:
    index_j = 0
    for j in i:
        if j%2==0:
            matrix[index_i][index_j] = 0
        index_j+=1
    index_i+=1


with open('File.txt_2', 'w') as my_file_2:
    my_file_2.write(json.dumps(matrix))
    my_file_2.close()
with open('File.txt_2') as my_file_2:
    print(json.load(my_file_2))

