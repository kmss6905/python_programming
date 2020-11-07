from collections import defaultdict
from collections import namedtuple

text = """
Apartments simplicity or understood do it we. Song such eyes had and off. Removed winding ask explain delight out few behaved lasting. Letters old hastily ham sending not sex chamber because present. Oh is indeed twenty entire figure. Occasional diminution announcing new now literature terminated. Really regard excuse off ten pulled. Lady am room head so lady four or eyes an. He do of consulted sometimes concluded mr. An household behaviour if pretended. 
""".lower().split()

word_count = defaultdict(lambda: 0)

for word in text:
    word_count[word] += 1

# from collections import OrderedDict


print(dict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)))

for k, v in dict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(k, v)
