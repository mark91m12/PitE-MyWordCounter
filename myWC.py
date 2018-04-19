from Logic import MyWordCounter
import sys

myWordCounter = MyWordCounter()


def run_wc():
    if len(sys.argv) == 1:
        return (myWordCounter.all_counts(sys.stdin))
    elif len(sys.argv) == 2:
        if sys.argv[1][0] == "-":
            if sys.argv[1] in myWordCounter.options:
                return (myWordCounter.functions[sys.argv[1]](sys.stdin))
            else:
                return ("MyWordCounter: invalid option\nTry 'python Logic.py -h' for more information.")
        else:
            try:
                txtFile = sys.argv[1]
                txtFile = open(txtFile, 'r')
                return (myWordCounter.all_counts(txtFile))
            except IOError:
                return ("MyWordCounter: ", txtFile, ": No such file or directory")

    elif len(sys.argv) == 3:
        if sys.argv[1] not in myWordCounter.options:
            return ("MyWordCounter: invalid option\nTry 'python Logic.py -h' for more information.")
        else:
            try:
                txtFile = sys.argv[2]
                txtFile = open(txtFile, 'r')
                return (myWordCounter.functions[sys.argv[1]](txtFile))
            except IOError:
                return ("MyWordCounter: ", txtFile, ": No such file or directory")
    else:
        return ("MyWordCounter: invalid input\nTry 'python Logic.py -h' for more information.")


if __name__ == '__main__':
    print(run_wc())
