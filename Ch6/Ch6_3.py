def count_word():
    _count = 0
    f = open('Ch6_Hey_Jude.txt')
    hey_jude_lyric = f.readlines()
    for line in hey_jude_lyric:
        print(
            line.strip().replace('-', ' ').replace('(', '').replace(')', '').replace(',', '').split(),
            len(line.strip().replace('-', ' ').replace('(', '').replace(')', '').replace(',', '').split())
        )
        _count = _count + len(line.strip().replace('-', ' ').split())
    return _count


print('전체 단어 수 : ', count_word())