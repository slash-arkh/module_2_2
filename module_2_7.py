def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() # работает
print_params(b = 25) # работает
print_params(c = [1,2,3]) # работает

values_list = [1, 'Модуль_2_7', True]
print_params(*values_list) #работает
values_dict = {'a': 'Словарь', 'b': True, 'c': 'Пройден'}
print_params(**values_dict) #работает

values_list_2 = [11, 'Барабанные палочки']
print_params(*values_list_2, 42) # все работает