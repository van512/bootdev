from stats import get_num_words, get_char_count, get_sorted_char_count
import sys

def get_book_text(path_to_file):
    """takes a filepath as input and returns the contents of the file as a string"""
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    dict_char_count = get_char_count(book_text)
    sorted_char_count = get_sorted_char_count(dict_char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_count:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    # This is the entry point of the program
    # It will be executed when the script is run directly
    # but not when it is imported as a module
    main()