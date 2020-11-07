max = {}
String = input().split()
itg = input().split()
for i in range(len(String)):
    max.setdefault(String[i], int(itg[i]))

max = {key:value for key,value in max.items() if value != 30 if value != max.get('delta')}
print(max)