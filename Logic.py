import sys

HELP_OPTION = "-h"
LINE_OPTION = "-l"
WORD_OPTION = "-w"
CHAR_OPTION = "-c"


class MyWordCounter():
    def __init__(self):
        self.options = [HELP_OPTION, LINE_OPTION, WORD_OPTION, CHAR_OPTION]
        self.lineCounter = self.wordCounter = self.charachterCounter = 0
        self.functions = {"-h": self.print_information,
                          "-l": self.count_lines,
                          "-w": self.count_words,
                          "-c": self.count_chars,
                          }

    def print_information(input):
        return "Usage: python MyWordCounter [OPTION]... [FILE]...\nWith no FILE read standard input.\n" \
               "The options below may be used to select which counts are printed, always in\n" \
               "the following order: newline, word, character.\n" \
               "-c           print the character counts\n" \
               "-l           print the newline counts\n" \
               "-w           print the word counts\n" \
               "-h           display this help" \

    def count_lines(self, input):
        for line in input:
            self.lineCounter += 1
        return "\n" + str(self.lineCounter)

    def count_words(self, input):
        for line in input:
            words = line.split()
            self.wordCounter += len(words)
        return "\n" + str(self.wordCounter)

    def count_chars(self, input):
        for line in input:
            self.charachterCounter += len(list(line))
        return "\n" + str(self.charachterCounter)

    def all_counts(self, input):
        for line in input:
            self.lineCounter += 1;
            words = line.split()
            self.wordCounter += len(words)
            self.charachterCounter += len(list(line))
        return "\n" + str(self.lineCounter) + " - " + str(self.wordCounter) + " - " + str(self.charachterCounter)

