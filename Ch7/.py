from collections import Counter
f = open("대한민국헌법_1장.txt", "r")
KoreanConstitution = f.readlines()
f.close()

contents = ""
for line in KoreanConstitution:
    contents = contents + line.strip() + "\n"

contents_change1 = contents.replace('[',' ')
contents_change2 = contents_change1.replace('.',' ')
contents_change3 = contents_change2.replace(',',' ')
contents_change4 = contents_change3.replace(']',' ')
contents_change5 = contents_change4.replace('①',' ')
contents_change6 = contents_change5.replace('②',' ')
contents_change7 = contents_change6.replace('③',' ')
contents_change8 = contents_change7.replace('④',' ')
contents_change9 = contents_change8.replace('⑤',' ')
contents_change10 = contents_change9.replace('⑥',' ')
contents_change11 = contents_change10.replace('⑦',' ')
contents_change12 = contents_change11.replace('ㆍ',' ')
contents_change13 = contents_change12.replace('<',' ')
contents_change14 = contents_change13.replace('>',' ')
content_list = contents_change14.split()
counter = Counter(content_list).most_common()
for i in range(10):
    print(counter[i][0])