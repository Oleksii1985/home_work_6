lst = [[1, None, 2, 3, 4+5j, 6], [1.0, 2.5, None, 3, 9, 4.0+5.2j, 6.1], ['1', '2', '3.6', None, '4+5.7j', '6']]

int_lst = []
float_lst = []
str_lst = []

for elem in lst:
    types = []
    for sym in elem:
        sym_type = type(sym)
        types.append(sym_type.__name__)
    single_types = []
    for i_types in types:
        if i_types not in single_types:
            single_types.append(i_types)
    types_count = []
    for element_type in single_types:
        type_count = types.count(element_type)
        types_count.append(type_count)
        max_types_count = max(types_count)
        index_max = types_count.index(max(types_count))
        main_type = single_types[index_max]
    separated_list = []
    for element in elem:
        if type(element).__name__ == main_type:
            separated_list.append(element)

    int_lst.extend(separated_list)
    float_lst.extend(separated_list)
    str_lst.extend(separated_list)

    res_int_lst = []
    [res_int_lst.append(k) for k in int_lst if type(k) == int]
    res_float_lst = []
    [res_float_lst.append(k) for k in float_lst if type(k) == float]
    res_str_lst = []
    [res_str_lst.append(k) for k in str_lst if type(k) == str]

print("integer list copy", int_lst)
print("float list copy", float_lst)
print("string list copy", str_lst)
print("list with integer type of numbers ", res_int_lst)
print("list with float type of numbers ", res_float_lst)
print("list with string type of numbers ", res_str_lst)
