from stats import get_number_of_words
from stats import count_characters
from stats import sorted_list_of_dictionaries
import sys
def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book = get_book_test(sys.argv[1])
    number_of_words = get_number_of_words(book)
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")

    print("--------- Character Count -------")
    number_of_characters = count_characters(book)
    sorted_list = sorted_list_of_dictionaries(number_of_characters) 
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['value']}")

    print("============= END ===============")

main()
