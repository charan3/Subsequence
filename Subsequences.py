import itertools
import random
import string
import math


def sub_sequences(lower_letter_string: str) -> str:
    combs = []
    dictionary = {}
    for l in range(1, len(lower_letter_string) + 1):
        combs.append(list(itertools.combinations(lower_letter_string, l)))
    for c in combs:
        for t in c:
            sub_seq = ''.join(t)
            if dictionary.get(sub_seq):
                dictionary[sub_seq] = dictionary[sub_seq] + 1
            else:
                dictionary[sub_seq] = 1
    maximum = 0
    value = ""
    for key in dictionary.keys():
        score = math.pow(len(key), 2) * math.pow((dictionary[key]-1), 0.33)
        if score > maximum:
            maximum = score
            value = key

    return value


def generate_random_letters_file(filename, size: float) -> None:
    chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(size))
    with open(filename, 'w') as f:
        f.write(chars)
    pass


generate_random_letters_file("random_letters_file.txt", 1024*1024*1024*3)  # 3GB = 1024*1024*1024*3
file = open("random_letters_file.txt", "r")
ls = file.read(3000)  # read 3000 characters from random_letter_file.txt
print("The subsequence with the highest score = " + sub_sequences(ls))
