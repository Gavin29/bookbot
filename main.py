def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    import sys
    from stats import get_num_words
    from stats import count_characters
    from stats import sort_output

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]

    book_content = get_book_text(book_path)

    word_count = get_num_words(book_path)

    count = count_characters(book_path)
    sorted_chars = sort_output(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_data in sorted_chars:
        char = char_data["char"]
        num = char_data["num"]

        if char.isalpha():
            print(f"{char}: {num}")       

    print("============= END ===============")

main()

    
