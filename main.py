def main():
    """
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()

    print(len(words))
    """
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    letter_dict ={}
    file_contents = file_contents.lower()
    for letter in file_contents:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    print(letter_dict)
main()