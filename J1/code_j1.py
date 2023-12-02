# Program by Imanuel Fehse

# Bundeswettbewerb Informatik
# Round 1
# Exercise Junior 1

# define decoding to get germans "Umlaute" right
# -*- coding: utf-8 -*-

# reference variables
vowels = ['a', 'e', 'i', 'o', 'u', 'ã', 'ö', 'ü']


# checks if rule 1 is true
def rule1():

    # check for pairs in definite vowel groups
    gv1 = definite_vowel_group
    gv2 = definite_vowel_group
    results = []
    for i in range(len(definite_vowel_group)):
        for j in range(len(definite_vowel_group)):

            # check if vowel pair is correct
            if gv1[i] == gv2[j] and i != j and [j, i] not in results:
                # check if the word endings are the same
                if word_endings[i] == word_endings[j]:
                    results.append([i, j])

    return results


# checks if results of rule one are also matching for rule 2
def rule2(results_rule1):
    results_rule2 = []
    for item in results_rule1:
        # get length of definite vowel group + wordending
        length = len(definite_vowel_group[item[0]]) + len(word_endings[item[0]])

        # if length is smaller or half of length of word
        if not length <= len(words[item[0]])/2 and not length <= len(words[item[1]])/2:
            results_rule2.append(item)
        else:
            pass

    return results_rule2


# checks if rule 3 is true
def rule3(results_rule2):
    results_rule3 = []
    for item in results_rule2:
        # check if word i ends with word j
        if words[item[0]].endswith(words[item[1]].lower()) or words[item[1]].endswith(words[item[0]].lower()):
            pass
        else:
            results_rule3.append(item)

    return results_rule3


# get vowel groups from word
def get_vowel_groups():

    # list to save vowels groups based on index
    vowel_group_list = []

    # loop trough every word
    for word in words:
        # list of vowel groups found in the word
        c_vowel_group_list = []
        # get length of word
        length = len(word)

        # loop through word
        i = 0
        while i < length:
            # variable for current vowel
            c_vowel = ""

            # if the i-th word is a vowel
            if word[i] in vowels:
                c_vowel = word[i]

                # if word still has letters after the i-th letter:
                if i+1 < length:
                    # check if letter after current letter is also a vowel
                    while i < length and word[i+1] in vowels:
                        c_vowel = c_vowel + word[i+1]
                        # increase i for next letter
                        i = i + 1

                        # if word still has letters after the i-th letter:
                        if i+1 < length:
                            pass
                        else:
                            break

            if c_vowel != "":
                # add vowel group to vowel_group_list
                c_vowel_group_list.append(c_vowel)

            # increase i to go to the next letter
            i = i + 1
        # add vowel groups of current word to list
        vowel_group_list.append(c_vowel_group_list)

    return vowel_group_list


def get_definite_vowel_group(list):

    # variable for definite group
    definite_group = []

    for item in list:
        if len(item) >= 2:
            definite_group.append(item[-2])
        elif item == []:
            definite_group.append("")
        else:
            definite_group.append(item[-1])

    return definite_group


def get_letters_after_definite_vowel(vowel_list, definite_vowels):

    endings = []
    for word in words:
        index_word = words.index(word)
        c_definite_vowel = definite_vowels[index_word]

        for i in range(len(word)):

            if word[:len(c_definite_vowel)] == c_definite_vowel:
                endings.append(word[len(c_definite_vowel):])
                break
            else:
                word = word[1:]

    return endings


while True:
    # get filename (and location) with words from userinput
    filename = input("\nPlease enter filename: ")

    # try to open file
    try:
        f = open(filename, "r", encoding="utf8")

    # if file does not exist
    except FileNotFoundError or OSError:
        print("No such file found")
        continue

    # read words from file
    words_raw = f.read().split()

    # make everything lowercase
    words = []

    for word_raw in words_raw:
        words.append(word_raw.lower())

    # get values from words
    # vowel groups of all words
    vowel_group_list = get_vowel_groups()
    # definite vowel grpous
    definite_vowel_group = get_definite_vowel_group(vowel_group_list)
    # letters after definite vowel
    word_endings = get_letters_after_definite_vowel(vowel_group_list, definite_vowel_group)

    results_rule1 = rule1()
    results_rule2 = rule2(results_rule1)
    results_rule3 = rule3(results_rule2)

    # print endresult of matching words
    print("\n")
    for item in results_rule3:
        print("Matching words:", words[item[0]], words[item[1]])
