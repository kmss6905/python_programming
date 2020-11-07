f = open('yesterday.txt')
yesterday_lyric = f.readlines()

contents = ""

for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"

n_of_yesterday = contents.count("yesterday")
print(n_of_yesterday)