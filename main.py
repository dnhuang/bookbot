from stats import count_words, count_characters, sort_list 
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = args[1]
    frankenstein_text = get_book_text(filepath)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    count_words(frankenstein_text)
    char_dict = count_characters(frankenstein_text)
    print('--------- Character Count -------')
    sorted_char_list = sort_list(char_dict)
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')

main()