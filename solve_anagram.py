from argparse import ArgumentParser
from itertools import permutations
from pathlib import Path
from typing import List

parser = ArgumentParser("anagram-solver")
parser.add_argument("letters")
args = parser.parse_args()

letters : List[str] = list(args.letters)

words_file = Path(__file__).parent / "google-10000-english" / "google-10000-english.txt"
words = set(words_file.read_text().split("\n"))

permutations = ["".join(letter_combo) for letter_combo in permutations(letters, len(letters))]

for possible_word in permutations:
    if possible_word in words:
        print(possible_word)

