def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f'Found {num_words} total words')
    return num_words
    
def count_characters(text):
    char_dict = {}
    for char in text:
        cleaned_char = char.lower()
        if cleaned_char not in char_dict:
            char_dict[cleaned_char] = 1
        else:
            char_dict[cleaned_char] += 1
    return char_dict

def sort_list(char_dict):
    def sort_on(items):
        return items['num']

    report_list = []
    for char, count in char_dict.items():
        report_list.append({"char": char, "num": count})
    report_list.sort(key=sort_on, reverse=True)
    return report_list