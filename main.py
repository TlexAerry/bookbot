def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    file_contents = file_contents.lower()
    words = file_contents.split()
    num_words = len(words)
    letter_dict ={}
    for letter in file_contents:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    print( "--- Begin report of books/frankenstein.txt ---")
    print(f"In books/frankenstein.txt there are a total of {num_words} words")
    
    for i in letter_dict:
        letter = i
        count = letter_dict[i]
        if letter.isalpha() == True:
            print(f"The '{letter}' character was found {count} times")
    print("--- End Report ---")
main()