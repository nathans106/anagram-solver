from argparse import ArgumentParser

parser = ArgumentParser("anagram-solver")
parser.add_argument("letters")
args = parser.parse_args()

letters : List[str] = args.letters.split()

