from nltk.tokenize import sent_tokenize, word_tokenize
import re
from enum import Enum

stock_dict={
    'DOW':['DOW', 'Dow Jones Industrial Average', 'Dow Industrial', 'the Dow', 'Dow Jones'],
    'UAL':['UAL', 'UAL Corp.', 'United Airlines'],
    'Blue Chip':['Blue Chip'],
    'AMR':['AMR', 'Alpha Metallurgical'],
    'American Airlines':['American Airlines', 'AAL'],
    'T. Rowe Price':['T. Rowe Price', 'TROW'],
    'Merril Lynch':['Merril Lynch', 'MER'],
    'Commerzbank AG':['Commerzbank AG', 'CRZBY'],
    'Jefferies':['Jefferies', 'JEF'],
    'Shearson':['Shearson', 'SHL'],
    'General Motors':['General Motors', 'GM'],
    'Procter & Gamble':['Procter & Gamble', 'PG'],
    'Kellogg Co.':['Kellogg Co.', 'K'],
    'Alcan Aluminum':['Alcan Aluminum', 'AAN'],
    'McDonalds':['McDonalds', 'MCD'],
    'Batterymarch':['Batterymarch', 'BTYM'],
    'S&P':['S&P', 'Standard and Poor', 'Standard & Poor'],
    'Ogallala':['Ogallala'],
    'IDS':['IDS', 'Identillect'],
}


GOOD_WORDS = [
    "[Gg]ain[ed]*",
    "[Cc]omeback",
    "[Ss]urge[ed]*",
    "[Ee]xploded*",
    "[Uu]pturn[ed]*",
    "[Rr]ecove[d|ry|r]",
    "[Rr]ebound[ed]*",
    "[Bb]urst",
    "[Bb]ought",
    "[Bb]uy",
    "[Tt]urn[ed]* up",
    "[hH]igh[er]*",
    "[uU]p",
    "[Rr][io]sen*",
    "[Jj]ump[ed]*"
]

BAD_WORDS = [
    "[Pp]lunged*",
    "[Ww]ere off",
    "[Ff][ea]ll[en]*",
    "[hH]ard hit",
    "[lL]os[te]",
    "[Cc]ollapsed*",
    "[Hh]urt[ing]*",
    "[dD]rop[ped]*",
    "[dD]eclined*",
    "[Cc]rash[ed]*",
    "[dD]rift[ed]*",
    "[cC]rush[ed]*",
    "[Tt]rouble[ed]*",
    "[dD]own[ed]*",
    "[Hh]its* bottom",
]



class Q_type(Enum):
    DID = 0
    WHAT = 1
    HOW = 2
    INVALID = 3


def question_cat(question: str) -> Q_type:
    if(re.search("\ADid", question) != None):
        return Q_type.DID
    if(re.search("\AWhat", question) != None):
        return Q_type.WHAT
    if(re.search("\AHow", question) != None):
        return Q_type.HOW
    return Q_type.INVALID


def question_open_or_close(question: str) -> bool:
    if re.search("[Oo]pen[ed]*", question) != None:
        return True
    if re.search("[Cc]lose[ed]*", question) != None:
        return False
    return None

def q_inc_or_dec(question: str) -> bool:
    if(question_cat(question) == Q_type.WHAT or question_cat(question) == Q_type.HOW):
        for g_word in GOOD_WORDS:
            if re.search(g_word, question) != None:
                print(g_word)
                return True
        for b_word in BAD_WORDS:
            if re.search(b_word, question) != None:
                print(b_word)
                return False
    return None

def find_line(question: str, filename: str):
    first_file = open(filename, "r")
    test1 = first_file.readlines()
    answers = []
    company_name = []
    for key in stock_dict:
        for word in stock_dict[key]:
            if question in stock_dict[key]:
                company_name = stock_dict[key]
    print(company_name)
    for line in test1:
        for name in company_name:
            if name in line:
                answers.append(line)
    return answers
    first_file.close()


def find_amt(company: str, line: str, question: str) -> str:
    word_list = []
    if q_inc_or_dec(question):
        word_list = GOOD_WORDS  
        print("good works being used")
    elif not q_inc_or_dec(question):
        word_list = BAD_WORDS
        print("bad words being used")
    match = ""
    for name in stock_dict[company]:
        if re.search(name, line) != None:
            print(name)
            match = re.search(name, line)
            numbers = re.findall("[0-9]+[.]*[0-9]*] | [0-9]+[\s]*[0-9]*[/]*[0-9]*", line)
            print(numbers)
            return "hi"
            



def main():
    first_file = open("test1.txt", "r")
    second_file = open("test2.txt", "r")
    test1 = first_file.read()
    test2 = second_file.read()
    first_file.close()
    second_file.close()
    sentence = "The Dow Jones Industrial Average jumped sharply yesterday to close at 2657.38, panic didn't sweep the world's markets, and investors large and small seemed to accept Friday's dizzying 3 1/2 190-point plunge as a sharp correction, not a calamity."
    find_amt('DOW', sentence, "How much did the Dow rise?")
    print("Done!")


if __name__ == "__main__":
    main()
