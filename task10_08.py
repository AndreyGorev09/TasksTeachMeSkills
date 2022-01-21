import csv

fields = 'Имя товара', 'цена', 'количество', 'комментарий'
rows = 'Phone', '200', '3', 'Super'


def write_csv():
    with open("csv_price_info.csv", "w") as my_file:
        csv_writs = csv.writer(my_file)
        csv_writs.writerow(fields)
        csv_writs.writerows(rows)

def read_csv():
    with open("csv_price_info.csv") as my_file:
        for col in fields:
            print(f'{col}\n', end='  ')
        print()
        for row in rows:
            print(f'{row}\n', end='  ')
    return

def rewrite_csv(list):
    with open("csv_price_info.csv", "a") as my_file:
        rewrite = csv.writer(my_file)
        rewrite.writerow(list)

print(read_csv())
print(rewrite_csv())
print(read_csv())
