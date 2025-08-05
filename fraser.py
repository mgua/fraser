#!/usr/bin/python
'''
this code was translated from the original fraser.pl perl code by mgua@tomware.it
translation was done by bing.ai on feb 12 2024

mgua@tomware.it

'''




import random

DEBUG = True
structures = ["sbj tv adv obj", "sbj adv tv obj", "sbj itv", "sbj pv sbj"]

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

s = random.choice(structures)  # Select a casual structure
print(s)
for p in s.split():
    if DEBUG:
        print(f"{p}:[", end="")
    print(random.choice(eval(p)), end="")
    if DEBUG:
        print("]", end="")
    print(" ", end="")
print('-') # final newline (printed string ends with a space)
