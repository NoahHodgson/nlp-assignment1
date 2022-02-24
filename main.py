from nltk.tokenize import sent_tokenize, word_tokenize

def question_cat(question: str) -> str:


def inc_or_dec(question: str) -> bool:


def find_line(company: str, inc_or_dec: bool) -> str:


def find_amt(company: str, line: str) -> int:



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
