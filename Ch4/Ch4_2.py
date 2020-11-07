# 윤년은 4의 배수이면서 100의 배수가 아닌 것 or 400의 배수인것
y = int(input())
if ((y%4) == 0 and (y % 100)!=0 ) or (y % 400) == 0:
    print("1")
else:
    print("0")