import sys

lineCounter = wordCounter = charachterCounter = 0
HELP_OPTION = "-h"
LINE_OPTION = "-l"
WORD_OPTION = "-w"
CHAR_OPTION = "-c"
options = [HELP_OPTION,LINE_OPTION,WORD_OPTION,CHAR_OPTION]

def print_information(input):
    print ("Usage: python MyWordCounter [OPTION]... [FILE]...\nWith no FILE read standard input.\n"
           "The options below may be used to select which counts are printed, always in\n"
           "the following order: newline, word, character.\n"
           "-c           print the character counts\n"
           "-l           print the newline counts\n"
           "-w           print the word counts\n"
           "-h           display this help")

def count_lines(input):
    global lineCounter
    for line in input:
        lineCounter += 1;
    print("\n",lineCounter)

def count_words(input):
    global wordCounter
    for line in input:
        words = line.split()
        wordCounter += len(words)
    print("\n",wordCounter)

def count_chars(input):
    global charachterCounter
    for line in input:
        charachterCounter += len(list(line))
    print("\n",charachterCounter)


def all_counts(input):
    global lineCounter, wordCounter, charachterCounter
    for line in input:
        lineCounter += 1;
        words = line.split()
        wordCounter += len(words)
        charachterCounter += len(list(line))
    print("\n",lineCounter," - ",wordCounter," - ",charachterCounter)

functions = {"-h" : print_information,
             "-l" : count_lines,
             "-w" : count_words,
             "-c" : count_chars,
}

if len(sys.argv) == 1:
    all_counts(sys.stdin)
elif len(sys.argv) == 2:
    if sys.argv[1][0] == "-":
        if sys.argv[1] in options:
            functions[sys.argv[1]](sys.stdin)
        else:
            print("MyWordCounter: invalid option\nTry 'python MyWordCounter.py -h' for more information.")
    else :
        try:
            txtFile = sys.argv[1]
            txtFile = open(txtFile, 'r')
            all_counts(txtFile)
        except IOError:
            print("MyWordCounter: ",txtFile,": No such file or directory")

elif len(sys.argv) == 3:
    if sys.argv[1] not in options:
        print("MyWordCounter: invalid option\nTry 'python MyWordCounter.py -h' for more information.")
    else :
        try:
            txtFile = sys.argv[2]
            txtFile = open(txtFile, 'r')
            functions[sys.argv[1]](txtFile)
        except IOError:
            print("MyWordCounter: ",txtFile,": No such file or directory")
else:
    print("MyWordCounter: invalid input\nTry 'python MyWordCounter.py -h' for more information.")



