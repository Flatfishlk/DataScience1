import itertools, numpy, random


# def sort_rows(mat):
#     result = []
#     for i in mat:
#         result.append(sorted(i))
#     return result

def sort_rows(mat):
    print [sorted(i) for i in mat]

M = [[2,3,1],[6,5,4]]
N = [[4, 5, 2, 8], [3, 9, 6, 7]]
# sort_rows(M)

def average_rows1(mat):
    print [numpy.mean(i) for i in mat]
# average_rows1(N)

def average_rows2(mat):
    print map(numpy.mean, mat)
# average_rows2(N)
# average_rows2(M)

# def word_length1(phrase):
#     result = []
#     for i in phrase.split():
#         result.append(len(i))
#     return result

p = "abc cde"
def word_length1(phrase):
    print [len(i) for i in phrase.split()]
# word_length1(p)

def word_length2(phrase):
    print map(len, phrase.split())
# word_length2(p)

# def even_odd1(L):
#     result = []
#     for i in L:
#         if i % 2 == 0:
#             result.append("even")
#         else:
#             result.append("odd")
#     return result
Q = [4,3,0,5,7,6]

def even_odd1(L):
    print ["even" if i % 2 == 0 else "odd" for i in L]

def even_odd2(L):
    print map(lambda x: "even" if x%2 == 0 else "odd", L)
# even_odd2(Q)

def shift_on_character(string, char):
    result = ""
    for i in range(len(string)):
        if string[i] == char:
            result = string[i:]+string[:i]
            break
    return result


def is_palindrome(string):
    return string == string[::-1]

# print is_palindrome("CCFCC")

def alternate(L):
    result1 = []
    result2 = []
    for i in range(len(L)):
        if i % 2 != 0:
            result1 += L[i]
    for i in range(len(L)):
        if i % 2 == 0:
            result2 += L[i]

    return result1 + result2

# print alternate(["a","b","c","d"])

def shuffle(L):
    half = len(L) // 2
    result1 = L[:half]
    result2 = L[half:]
    result = []
    for i in range(half):
        result.append(result1[i])
        result.append(result2[i])
    return result

def filter_words(word_list, letter):
    result = []
    for i in range(len(word_list)):
        if word_list[i][0] == letter:
            result.append(word_list[i])
    return result

def factors(num):
    result = []
    for i in range(num+1):
        if num % (i+1) == 0:
            result.append(i+1)
    return result


def acronym(phrase):
    print ["".join(i[0] for i in phrase.split()).upper()]

def sort_by_ratio(L):
    print sorted(L, key = lambda x: (float(x[0])/x[1]))

# sort_by_ratio([(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)])

def count_match_index(L):
    result = 0
    for i, j in enumerate(L):
        if i == j:
            result += 1
    return result

# print count_match_index([0, 2, 2, 3, 6, 5])

# def only_sorted(L):
#     result = []
#     for i in L:
#         if i == sorted(i):
#             result.append(i)
#     return result
# print only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])

def only_sorted(L):
    print [x for x in L if x == sorted(x)]
# only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])

def concatenate(L1, L2, connector=""):
    zipped = [connector.join((x, y)) for x, y in zip(L1, L2)]
    return zipped
# print concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    # ["California", "New York", "Nevada", "California"], ", ")
def transpose(mat):
    print[list(x) for x in zip(*mat)]
# transpose([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

def invert_list(L):
    result = {}
    for i, j in enumerate(L):
        result.update({j:i})
    return result
# print invert_list(['a', 'b', 'c', 'd'])

def digits_to_num(digits):
    print reduce(lambda x, y: x*10+y, digits)
# digits_to_num([5, 0, 3, 8])

def intersection_of_sets(l):
    print reduce(set.intersection, l)
# intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])

def combinations(a, n):
    result = []
    for i in range(n):
        result += ["".join(x) for x in (list(tup) for tup in itertools.combinations(a, i+1))]
        # result += ["".join(map(str,itertools.combinations(a, i+1)))]
    return result
# print combinations('abc', 3)

def permutations_in_dict(string, words):
    result = []
    for i in ["".join(x) for x in (list(itertools.permutations(string, len(string))))]:
        for j in words:
            if i == j:
                result.append(i)
    return result

print permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
