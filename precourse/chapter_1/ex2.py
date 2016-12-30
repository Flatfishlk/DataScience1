import string, sys

def word_counts(f):
    result = {}
    mtext = f.translate(None, string.punctuation).lower()
    for i, x in enumerate(mtext.split()):
        if i < len(mtext.split())-1:
            result[x] = {} if not x in result else result[x]
            if mtext.split()[i+1] in result[x]:
                result[x][mtext.split()[i+1]] += 1
            else:
                result[x][mtext.split()[i+1]] = 1
    return result

# print word_counts("The cat chased the dog")
def associated_words(f):
    with open("alice_testout.txt","w") as o_f:
        with open (f, "r") as i_f:
            data = i_f.read()
            result = {}
            mf = data.translate(None, string.punctuation).lower().split()
            for i, x in enumerate(mf):
                if i < len(mf)-2:
                    s, t = mf[i], mf[i+1]
                    tup = (s, t)
                    result[tup] = [] if not tup in result else result[tup]
                    if mf[i+2] not in result[tup]:
                        result[tup].append(mf[i+2])

        o_f.write(str(result))
        o_f.close

# associated_words("alice.txt")

import numpy, random
with open("alice_testout.txt","r")
def make_random_story(f, num_words):
    result = []
    i = 0
    while i < 2:
        tup = random.choice(f.keys())
        result.append(random.choice(f[tup]))
        i += 1
    for n, x in enumerate(result):
        if n >= 1:
            tup1 = (result[n-1], result[n])
            for m in f:
                if tup1 == m:
                    result.append(random.choice(f[tup1]))
                else:
                    result.append(random.choice(f[tup]))
        if n == num_words-2:
            break
    print result

make_random_story({("a","b"):["a","b"], ("b","b"):["b","a"], ("a","a"):["a","b"], ("b","a"):["a","b"]}, 4)
