#Import functions from stats.py
import sys
from stats import word_count, char_count, sorting_by_char_count

try:
    sys.argv[1]
    print("Usage: python3 main.py <path_to_book>")
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]

# Function to read the text from a text file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



    
# Function to test other functions
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print("Found", word_count(f"{filepath}"), "total words")
    print("--------- Character Count -------")
    character_count = char_count(f"{filepath}")
    all_chars = sorting_by_char_count(character_count)
    for char_dict in all_chars:
        # Get the first (and only) key from the dictionary
        char = list(char_dict.keys())[0]
        if char.isalpha():  # Check if it's an alphabetical character
            count = char_dict[char]
            print(f"{char}: {count}")
    print("============= END ===============")

main()