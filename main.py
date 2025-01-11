BOOK_PATH = "books/frankenstein.txt"
def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        print_book_report(file_contents)

def get_num_words(text):  
    print(len(text.split()))

def get_chars_dict(text):
    characters = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in characters:
            characters[lower_char] += 1
        else:
            characters[lower_char] = 1

    return characters

def print_book_report(text):
    report = f"--- begin report of {BOOK_PATH} ---"
    report += f"\n{get_num_words(text)} words found in the document\n"
    characters = get_chars_dict(text)
    for char in characters:
        if char.isalpha():
            report += f"\nThe '{char}' character was found {characters[char]} times"
    print(report)
    

main()