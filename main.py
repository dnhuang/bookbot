def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #print(f"words in frankenstein: {count_words(text)}")
    character_dict = count_char(text)
    #print(character_dict)
    letter_report(character_dict, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    lower_text = text.lower()
    char_dict = {}

    for character in lower_text:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    return char_dict

def sort_on(key):
    return key["count"]

def letter_report(char_dict, path):
    letters = []
    for character in char_dict:
        if character.isalpha():
            letters.append({"char":character, "count":char_dict[character]})
    letters.sort(key=sort_on, reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{count_words(get_book_text(path))} words found in the document\n")
    for letter in letters:
        print(f"The '{letter["char"]}' character was found {letter["count"]} times")
    return letters


main()