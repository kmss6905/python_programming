
f = open('파이썬2_수강생_이름.txt')
name = []
for i in f.readlines():
    name.append(i.replace('\n', ''))
# print(name)

f_numbers = open('파이썬2_수강생_학번.txt')
numbers = []
for i in f_numbers.readlines():
    numbers.append(i.replace('\n', ''))
# print(numbers)


f_department = open('파이썬2_수강생_학과.txt')
departments = []
for i in f_department.readlines():
    departments.append(i.replace('\n', ''))
# print(departments)

# 1번
_list = list(zip(name, numbers, departments))
print('1번', _list, '\n', '*'*100)

# 2번
dict_a = {i: [v1, v2] for i, v1, v2 in _list}
print('2번', dict_a, '\n', '*'*100)

# 3번
sorted_tuple_list_by_name = sorted(_list, key=lambda x: x[0])
sorted_dict_by_name = {i: [v1, v2] for i, v1, v2 in sorted_tuple_list_by_name}
print('3번', sorted_dict_by_name, '\n', '*'*100)

# 4번
print('4번')
sorted_tuple_list_by_num = sorted(_list, key=lambda x: x[1])
print("{0} {1} {2:^30} {3}".format("No", "학번", "이름", "법학과"))
for i, value in enumerate(sorted_tuple_list_by_num):
    # print(i, format(value[1], "10"), format(value[0], "16"), value[2])
    a = "{i} {v0} {v1:^30} {v2}".format(i=i, v0 = value[0], v1 = value[1], v2 = value[2])
    print(a)















