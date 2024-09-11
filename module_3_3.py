def print_params(a = 1, b = 'Strting', c = True):
    print(a, b, c)
    print()
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

list_ = ['Viktor', 123, False]
values_list = ['Anna', 123]
values_dict = {'c':42}
print_params(*list_)
print_params(*values_list, 23)
print_params(*values_list,**values_dict)
values_list_2 = [54.32, 'String']
print_params(*values_list_2, 42)