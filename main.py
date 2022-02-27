from nltk.tokenize import sent_tokenize, word_tokenize
import re
from enum import Enum

GOOD_WORDS = [
    "\[Gg]ain*ed",
    "\[Cc]omeback",
    "\[Ss]urge*ed",
    "\[Ee]xplode*d",
    "\[Uu]pturn*ed",
    "\[Rr]ecove*d|ry|r",
    "\[Rr]ebound|ed",
    "\[Bb]urst",
    "\[Bb]ought",
    "\[Bb]uy",
    "\[Tt]urn*ed up",
    "\[hH]igh*er",
    "\[uU]p"
]

BAD_WORDS = [
    "\[Pp]lunge*d",
    "\[Ww]ere off",
    "\[Ff][ea]ll*en",
    "\[hH]ard hit",
    "\[lL]os[te]",
    "\[Cc]ollapse*d",
    "\[Hh]urt*ing",
    "\[dD]rop*ped",
    "\[dD]ecline*d",
    "\[Cc]rash*ed",
    "\[dD]rift*ed",
    "\[cC]rush*ed",
    "\[Tt]rouble*ed",
    "\[dD]own*ed",
    "\[Hh]it*s bottom",
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


def q_inc_or_dec(question: str) -> bool:
    if(question_cat(question) == Q_type.WHAT or question_cat(question) == Q_type.HOW):
        for g_word in GOOD_WORDS:
            if g_word in question:
                return True
        for b_word in BAD_WORDS:
            if b_word in question:
                return False
    return None


def find_line(company: str, inc_or_dec: bool) -> str:
    return


def find_amt(company: str, line: str) -> int:
    return


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
