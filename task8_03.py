dict = {'key': 'value', 'metod': 'funce'}
print(dict)

list_key = list(dict.keys())
list_volue = list(dict.values())
new_dict = {}
new_dict.update(zip(list_volue,list_key))
print(new_dict)