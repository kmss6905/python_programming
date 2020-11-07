from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(10, 10, 20)
print(p.__doc__)