from stats import get_num_words, get_num_characters, get_sorted_characters
from sys import argv, exit

def get_book_text(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
        return file_contents

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)
    num = get_num_words(text)
    characters = get_num_characters(text)
    sorted_characters = get_sorted_characters(characters)

    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["count"]}")
    print("============= END ===============")

main()