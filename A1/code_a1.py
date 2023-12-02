# Program by Imanuel Fehse

# Bundeswettbewerb Informatik
# Round 1
# Exercise A1

# -*- coding: utf-8 -*-

import re

# FILES
# story : Alice im Wunderland
filename_alice = "Alice_im_Wunderland.txt"


def convert_search(searching):
    s = searching.split(" ")
    result = ""
    # for every word in search request
    for i in range(len(s)):
        # if this is a searched word
        if s[i] == "_":
            # add empty to pattern
            # if its the first word in search request
            if i == 0:
                # add without space
                result += "[^\s]+"
            else:
                # add with space
                result += "\s[^\s]+"
        # if the word is given
        else:
            # add word to pattern
            # if its the first word in search request
            if i == 0:
                # add without space
                result += s[i]
            else:
                # add with space
                result += "\s" + s[i]

    return result


def search(pattern):
    # get story and make it lower case
    text = open(filename_alice, "r", encoding="utf8").read().lower().replace("\n", " ")
    # keep only necessary (no punctuation etc.)
    # pattern only alphabetic characters and spaces
    substract_pattern = re.compile('[\W_]+' + '|' + '\s+')
    text = substract_pattern.sub(' ', text)
    # search and print results
    print(re.findall(pattern, text))


while True:
    # get file with search-request
    filename = input("\nPlease enter filename: ")
    try:
        f = open(filename, "r", encoding="utf8")
    except FileNotFoundError:
        print("File not found. Please try again.")
        continue

    # get searched sequence from file
    searched_sentence = f.read()
    pattern = re.compile(convert_search(searched_sentence))

    # search in story
    search(pattern)
