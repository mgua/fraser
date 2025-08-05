#!/usr/bin/python
'''
this code was translated from the original fraser.pl perl code by mgua@tomware.it
translation was done by bing.ai on feb 12 2024

mgua was improving the translation, rewriting small portions in more pythonic ways

mgua@tomware.it

'''


import random

DEBUG = True
structures = ["sbj tv adv obj", "sbj adv tv obj", "sbj itv", "sbj pv sbj"]

addinits = []
addendings = []
for s in structures:
    addinits.append("init " + s)
for s in structures:
    addendings.append(s + " ending")

structures = structures + addinits
structures = structures + addendings


# Inits
init = ['once upon a time', 'Once in a while', 'Finally', 'it was time for', 'you wont believe that', 'do you know that', 'Unexpectedly']

# Endings
ending = ['and everybody was happy', 'while nobody cares', 'and so goes life', 'and good luck', 'and thanks']

# Subjects
sbj = ["the man", "the woman", "a kangaroo", "a turtle",
       "my cousin's dog", "a white cat", "a donkey",
       "the small yellow bird", "a big elephant",
       "Fred", "Dorothy", "Helen", "Jack"]

# Passive verbs
pv = ["was killed by", "was hit by"]

# Intransitive verbs (don't want a target entity)
itv = ["ran away", "was crying", "was laughing", "jumped", "fell down"]

# Transitive verbs (want a target entity)
tv = ["eat", "ate", "loves", "kissed", "licked", "greeted",
      "killed", "kicked in the ass"]

# Adverbs
adv = ["gently", "strongly", "fiercely", "softly", "barely",
       "kindly", "rudely", "passionately"]

# Objects
obj = ["a dead fish", "the policeman", "a jazzman",
       "a clown", "a kid", "the princess",
       "one passing man", "a nude woman", "a painting"]

s = random.choice(structures)  # Select a random structure
print(s)
myline = []
for p in s.split(): # split on whitespace
    elem = random.choice(eval(p))
    if DEBUG:
        myline.append(f'{p}:[{elem}]')
    else:
        myline.append(f'{elem}')
print(' '.join(myline)) 

