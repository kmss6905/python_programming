# 단어 횟수 세기 - jude 가 몇개
# 단어 횟수 Na 또는 na
# 단어 변경하여 가사 말 출력 jude -> 본인 이름으로 변경
def count_jude():
    n_of_jude = 0
    contents = ""
    f = open('Ch6_Hey_Jude.txt')
    hey_jude_lyric = f.readlines()
    for line in hey_jude_lyric:
        contents = contents + line.strip() + "\n"
    n_of_jude = contents.count("Jude")
    return n_of_jude


def count_na():
    n_of_na = 0
    contents = ""
    f = open('Ch6_Hey_Jude.txt')
    hey_jude_lyric = f.readlines()
    for line in hey_jude_lyric:
        contents = contents + line.strip().lower() + "\n"

    n_of_na = contents.count("na")
    return n_of_na

def change_name_to_minshik():
    n_of_na = 0
    contents = ""
    f = open('Ch6_Hey_Jude.txt')
    hey_jude_lyric = f.readlines()
    for line in hey_jude_lyric:
        contents = contents + line.strip().replace('Jude', 'MinShik') + "\n"
    return contents

print('jude word count is : ', count_jude())
print('Na/na word count is : ', count_na())
print("-"*100,'\n',change_name_to_minshik())
