# num = 0
# # sum = 0
# # while num <= 1000:
# #     num += 1
# #     print(num, " 번 쨰")
# #     if( num % 3 == 0):  # 3의 배수 일 경우
# #         sum = sum + num
# #         print(sum)
# import sys
# args = sys.argv[1:]
#
#
# def num_star(num: int):
#     i = 0
#     while (i < num):
#         i += 1
#         print("*" * i)
#
#
# num_star(5)
#
# # Q4
# for i in range(101):
#     print(i)
#
# # Q5
#
# scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#
#
# def mean_scores(scores):
#     total_score = 0
#     for score in scores:
#         total_score += score
#     mean_score = total_score / len(scores)
#     return mean_score
#
#
# print('A 학급의 평균점수 = ', mean_scores(scores))
#
#
#
#
#
# #Q6
#
# number = [1, 2, 3, 4, 5]
# result = [i*2 for i in number if i % 2 == 1]
# print(result)
#
#
#
# ### 제 4장 연습문제
#
# # Q5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
#
# f1 = open("test.txt", 'r')
# print(f1.read())




def write_file(args):
    if (len(args) != 0):
        for arg in args:
            f = open("test.txt", 'a')
            f.write(arg)


def replace_words(file_name, _from, _to):
    print(file_name)
    f = open("test.txt", 'a')
    for line in list(f.readlines()):
        if str(_from) in line:
            c_line = line.replace(str(_from), str(_to))
            print(c_line)




if __name__ == '__main__':
    # args = sys.argv[1:]
    # write_file(args)
    import sys
    replace_words(sys.argv[1], sys.argv[2], sys.argv[2])




