from nltk.tokenize import sent_tokenize, word_tokenize
import re
from enum import Enum

from numpy import true_divide

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
    "[Rr][io]sen*"
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


def find_line(question: str, filename: str) -> str:
    first_file = open("test1.txt", "r")
    test1 = first_file.readlines()
    for line in test1:
        print("here")

    first_file.close()


def find_amt(company: str, line: str) -> int:
    return


def main():
    first_file = open("test1.txt", "r")
    second_file = open("test2.txt", "r")
    test1 = first_file.read()
    test2 = second_file.read()
    first_file.close()
    second_file.close()
    print(question_cat("How much did the S&P drop?"))
    print(q_inc_or_dec("How much did the S&P drop?"))
    print(q_inc_or_dec("How much did IBM go up?"))
    print("Done!")


if __name__ == "__main__":
    main()
