import sys
import random

word_list = []

def produce_words(_word_list = word_list):
    string_input = ""
    if type(_word_list) == list:
        string_input.join(_word_list)
    else:
        string_input = _word_list
    vowel_list = ""
    consonant_list = ""
    for c in string_input.lower():
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel_list = vowel_list + c
        else:
            consonant_list = consonant_list + c
    
    format_strings = ['011010', '01011010100', '010110', '000101', '01010010', '001010010', '000101', '01010010', '001010010', '010101010']

    total_output = ""
    for j in range(10):
        # make a random word
        out = ""

        format_string = format_strings[random.randint(0, len(format_strings) - 1)]

        for char in range(len(format_string)):
            if format_string[char] == "0":
                # pick consonant
                out = out + consonant_list[random.randint(0, len(consonant_list) - 1)]
            else:
                # pick vowel
                out = out + vowel_list[random.randint(0, len(vowel_list) - 1)]
        
        total_output = total_output + out + '\n'
    return total_output

def main():
    word_list = initialize(sys.argv)
    total_output = "Output words:\n=================\n"
    total_output = total_output + produce_words(word_list)
    total_output = total_output + '================='
    print(total_output)

def initialize(arguments):
    _word_list = ""
    try:
        if len(arguments) == 1:
            _word_list = open("word_list.txt", "r").read().replace("\n", "")
        elif ('word_list.txt' or '.\\word_list.txt' or '.\word_list.txt') in arguments[1]: 
            _word_list = open("word_list.txt", "r").read().replace("\n", "")
        elif '.txt' in arguments[1]:
            _word_list = open(arguments[1], "r").read().replace("\n", "")
        else:
            _word_list = ""
            for word in arguments[1:]:
                _word_list = _word_list + "\n" + word
            _word_list = _word_list.replace("\n", "")
        return _word_list
    except:
        print ("Usage: python word_randomizer.py word_list.txt OR python word_randomizer.py [list of words to use as base]")
        return

main()