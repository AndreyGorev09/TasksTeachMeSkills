list_name_car = [{'bmw': {'1HGEG644387712345': 1999}},
                 {'mersedes': {'1HHJG644837252349': 2010}},
                 {'audi': {'1HGND644391237346': 2014}},
                 {'toyota': {'1WEEG649812612341': 2012}}]

list_value_year_car = []
new_list_value_year_car = []
n = int(2010)

for x in list_name_car:
    for i in x.values():
        for f in i.values():
            if f > n:
                new_list_value_year_car.append(x.copy())
print(new_list_value_year_car)