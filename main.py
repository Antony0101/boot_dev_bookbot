def main():
   path = "./books/frankenstein.txt"
   data = get_file_data(path)
   words = count_words(data)
   letters = count_letters(data)
   print_report(words, letters)

def get_file_data(path):
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(data):
    words = data.split()
    return len(words)

def count_letters(data):
    dict = {}
    newData = data.lower()
    for letter in newData:
        if letter.isalpha():
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
    return dict

def sort_on(d):
    return d['num']

def print_report(words, letters):
    # covert letters dict to list of dict with key letter and value count
    letter_list = []
    for key, value in letters.items():
        temp = {"letter": key, "num": value}
        letter_list.append(temp)
    letter_list.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    for letter in letter_list:
        print(f"The {letter["letter"]} character was found {letter["num"]} times")
    print("--- End report ---")

main()