import re
import nltk
from nltk.corpus import wordnet as wn

def tagger(sentence):
    text = sentence.split()
    taggedText = nltk.pos_tag(text)

    print(taggedText)
    return taggedText


text = input()
text = text.lower()
Taggedtext = tagger(text)

#converting tags into simpler ones as used in the paper
# use this to see all possible tags nltk.help.upenn_tagset()
countV, countN, countA, countR = 0, 0, 0, 0 #for similarity measures
listV, listN, listA, listR = [], [], [], []

for i in range(len(Taggedtext)):
    old = Taggedtext[i][1]
#for verb
    match = re.match(r'VB*', old)
    if match:
        Taggedtext[i] = (Taggedtext[i][0],'VB')
        listV.append(TaggedText[i][0]
        countV += 1
#for noun
    match = re.match(r'NN*', old)
    if match:
        Taggedtext[i] = (Taggedtext[i][0],'NN')
        countN += 1
        listN.append(TaggedText[i][0]
#for adjectives
    match = re.match(r'JJ*', old)
    if match:
        Taggedtext[i] = (Taggedtext[i][0],'JJ')
        countA += 1
        listA.append(TaggedText[i][0]
#for adverb
    match = re.match(r'RB*', old)
    if match:
        Taggedtext[i] = (Taggedtext[i][0],'RB')
        countR += 1
        listR.append(TaggedText[i][0]


print(Taggedtext)

