from nltk.tokenize import sent_tokenize, word_tokenize
def main():
    first_file = open("test1.txt", "r")
    second_file = open("test2.txt", "r")
    test1 = first_file.read()
    test2 = second_file.read()
    first_file.close()
    second_file.close()
    print("Done!")

if __name__ == "__main__":
    main()
