list_group = [{'firstname':'Masha', 'Group': 42, 'phisics': 6, 'informatics': 4, 'history': 8},
              {'firstname':'Pasha', 'Group': 42, 'phisics': 5, 'informatics': 7, 'history': 6},
              {'firstname':'Misha', 'Group': 42, 'phisics': 8, 'informatics': 6, 'history': 9}]
for a in list_group:
    averange = (int(a['phisics']) + (a['informatics']) + (a['history'])) / 3
    if averange > 4:
        print(f"Средний балл {a['firstname']} из группы {a['Group']}: {averange}")