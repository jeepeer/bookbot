def main():
    with open("/home/test/workspace/github.com/jeepeer/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

main()