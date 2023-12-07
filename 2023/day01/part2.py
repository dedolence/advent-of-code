import re
"""
    two1nine            = 29
    eightwothree        = 83
    abcone2threexyz     = 13
    xtwone3four         = 24
    4nineeightseven2    = 42
    zoneight234         = 14
    7pqrstsixteen       = 76
"""
FILENAME = "test.txt"
ANSWER = 0
INPUT = []
WORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
         "six": "6", "seven": "7", "eight": "8", "nine": "9"}
""" 
    The danger of replacing words with their number equivalent by looping over the
    dict of words-to-integers in a for loop is that "one" will always get replaced 
    before "two", even in the case of a line that contains "twone," which will get
    converted to "tw1" instead of what we want: "2ne". 
    we need the FIRST word to be converted, regardless of its integer value. 
"""

input = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

def convert_words(line):
    # find the earliest index of each word that occurs
    i_list = []

""" 
for line in input:
    line = [line.replace(k, v) for (k, v) in WORDS.items() if k in line]
    ['21nine', 'two19']
    ['eigh2three', 'eightwo3', '8wothree']
    ['abc12threexyz', 'abcone23xyz']
    ['xtw13four', 'x2ne3four', 'xtwone34']
    ['4nineeight72', '4nine8seven2', '49eightseven2']
    ['z1ight234', 'zon8234']
    ['7pqrst6teen']
"""
print(ANSWER)