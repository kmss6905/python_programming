from collections import Counter


def main():
    text_line = open("대한민국헌법_1장.txt").readlines()
    c = Counter()
    for line in text_line:
        c += Counter(un_special_chars(line))  # 라인 별로 counter 함수를 구해 기존에 구했던 counter 에 다시 더함
    print(c.most_common(10))  # 내림차순으로 가장 빈번하게 등장하는 단어 10개를 (단어, 개수) 형태의 tuple list 로 출력


def un_special_chars(s: str):
    """
    입력값으로 문자열에서 특수문자를 제거한 후 단어로 구분되어 있는 리스트를 출력하는 함수
    :param s: 문자열
    :return: 리스트
    """
    for char in special_chars:  # 쉼표, 마침표, 화살표 등등 의 특수문자 제거
        s = s.replace(char, ' ')
    for i in range(1, 21):  # 원숫자 제거
        s = s.replace(chr(0x245f + i), ' ')
    return s.strip().split()  # 리스트에 담음


if __name__ == '__main__':
    special_chars = ['\u2219', '\u2023', '\u2022', '\u318D', '\u30FB', '\u2022', '\u003C', '\u003E', '\u002C', '\u005B',
                     '\u005D', '\u002E']
    main()
