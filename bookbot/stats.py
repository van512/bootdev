def get_num_words(text: str) -> int:
    """accepts the text from the book as a string, and returns the number of words in the string"""
    words = text.split()
    return len(words)

def get_char_count(text: str) -> dict:
    """ takes the text from the book as a string, 
    and returns the number of times each character, 
    (including symbols and spaces), appears in the string."""
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def get_sorted_char_count(char_count: dict) -> list:
    """takes the dictionary of characters and their counts 
    and returns a sorted list of dictionaries"""
    sorted_list = []
    for char, count in char_count.items():
        sorted_list.append({"char": char, "num": count})
        sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
