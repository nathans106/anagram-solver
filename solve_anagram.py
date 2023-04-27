import sys
from argparse import ArgumentParser
from itertools import permutations
from pathlib import Path
from typing import List

def parse_words(file: Path) -> set:
    return set(file.read_text().split("\n"))

parser = ArgumentParser("anagram-solver")
parser.add_argument("letters")
args = parser.parse_args()

letters : List[str] = list(args.letters)

words = parse_words(Path(__file__).parent / "google-10000-english" / "20k.txt")
words = words.union(parse_words(Path(__file__).parent / "english-words" / "words_alpha.txt"))

permutations = ["".join(letter_combo) for letter_combo in permutations(letters, len(letters))]

matches = set([word for word in permutations if word in words])

if len(matches) == 0:
    print("No matches found")
    sys.exit(1)

for match in matches:
    print(match)

sys.exit(0)
