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

    def run_WC(self):
        if len(sys.argv) == 1:
            print(self.all_counts(sys.stdin))
        elif len(sys.argv) == 2:
            if sys.argv[1][0] == "-":
                if sys.argv[1] in self.options:
                    print(self.functions[sys.argv[1]](sys.stdin))
                else:
                    print("MyWordCounter: invalid option\nTry 'python MyWordCounter.py -h' for more information.")
            else:
                try:
                    txtFile = sys.argv[1]
                    txtFile = open(txtFile, 'r')
                    print(self.all_counts(txtFile))
                except IOError:
                    print("MyWordCounter: ", txtFile, ": No such file or directory")

        elif len(sys.argv) == 3:
            if sys.argv[1] not in self.options:
                print("MyWordCounter: invalid option\nTry 'python MyWordCounter.py -h' for more information.")
            else:
                try:
                    txtFile = sys.argv[2]
                    txtFile = open(txtFile, 'r')
                    print(self.functions[sys.argv[1]](txtFile))
                except IOError:
                    print("MyWordCounter: ", txtFile, ": No such file or directory")
        else:
            print("MyWordCounter: invalid input\nTry 'python MyWordCounter.py -h' for more information.")


if __name__ == '__main__':
    MyWordCounter().run_WC()
