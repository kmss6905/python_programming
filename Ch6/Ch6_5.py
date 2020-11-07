# 51900;83000;158000;367500;250000;59200;128500;1304000

_list = list(input().split(';'))
price_list = []
for i in _list:
    price_list.append(int(i))


def print_result():
    price_list.sort(reverse=True)
    for price in price_list:
        _s = '{:>9,}'.format(price)
        print(_s)

print_result()