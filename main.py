def main():
    with open("/home/test/workspace/github.com/jeepeer/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        #print(wordCounter(file_contents))
        print(get_chars_dict(file_contents))

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

main()