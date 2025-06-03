from stats import wc
from stats import char
from stats import sorted
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text(sys.argv[1]))

book_text = get_book_text(sys.argv[1])

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {wc(book_text.split())} total words")
print("--------- Character Count -------")

for item in sorted(char(book_text)):
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")

print("============= END ===============")       