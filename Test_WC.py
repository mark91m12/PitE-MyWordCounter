import unittest
import sys
from Logic import MyWordCounter

mock_text = ["this is a test\n", "with 3 lines, 12 words and \n", "57 characthers"]


class TestMyWC(unittest.TestCase):


    def test_lines(self):
        result = (MyWordCounter().count_lines(mock_text))
        self.assertEqual(result, "\n3")

    def test_words(self):
        result = (MyWordCounter().count_words(mock_text))
        self.assertEqual(result, "\n12")

    def test_chars(self):
        result = (MyWordCounter().count_chars(mock_text))
        self.assertEqual(result, "\n57")

    def test_all_results(self):
        result = (MyWordCounter().all_counts(mock_text))
        self.assertEqual(result, "\n3 - 12 - 57")

    def test_info(self):
        info = "Usage: python MyWordCounter [OPTION]... [FILE]...\nWith no FILE read standard input.\n" \
               "The options below may be used to select which counts are printed, always in\n" \
               "the following order: newline, word, character.\n" \
               "-c           print the character counts\n" \
               "-l           print the newline counts\n" \
               "-w           print the word counts\n" \
               "-h           display this help"

        result = (MyWordCounter().print_information())
        self.assertEqual(result, info)

if __name__ == '__main__':
    unittest.main()