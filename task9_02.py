list_names = ['Andrei', 'Lisa', 'Nika', 'Igor', 'Riki', 'Ann', 'Katy']
new_list_names = list(map(lambda names: f'Hello, {names}', list_names))
print(new_list_names)
