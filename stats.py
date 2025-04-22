def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)
    
def char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        chars = {}
        for char in file_contents:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        return chars

def sort_on(char_dict):
    # Extract the first (and only) key from the dictionary
    char = list(char_dict.keys())[0]
    # Return the value associated with that key
    return char_dict[char]

def sorting_by_char_count(char_count):
    sorted_chars = []
    for char in char_count:
        sorted_chars.append({char: char_count[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars