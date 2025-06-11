def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    return word_count

def count_characters(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
    
    file_contents = file_contents.lower()
    
    num_characters = {}

    for char in file_contents:
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters

def sort_output(num_characters):
    char_list = []
    for char, count in num_characters.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list