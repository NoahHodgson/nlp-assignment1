from typing import List
import re
from enum import Enum

stock_dict={
    'DOW':['DOW', 'Dow Jones Industrial Average', 'Dow Industrial', 'the Dow', 'Dow Jones'],
    'UAL':['UAL', 'UAL Corp.', 'United Airlines'],
    'AMR':['AMR', 'Alpha Metallurgical'],
    'American Airlines':['American Airlines', 'AAL'],
    'T. Rowe Price':['T. Rowe Price', 'TROW'],
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
    "DIS": ['Disney', "Walt Disney"],
    'IBM': ['IBM'],
    "None": ["No Business"]
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
    "[Rr][io]sen*",
    "[Jj]ump[ed]*"
]

BAD_WORDS = [
    "[Pp]lunged*",
    "[Ww]ere off",
    "[Ff][ea]ll[en]*",
    "[hH]ard hit",
    "[lL]os[te]+[\s|.]+",
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


def q_open_or_close(question: str) -> bool:
    if re.search("[Oo]pen[ed]*", question) != None:
        return True
    if re.search("[Cc]lose[ed]*", question) != None:
        return False
    return None

def q_inc_or_dec(question: str) -> List[str]:
    for g_word in GOOD_WORDS:
        if re.search(g_word, question) != None:
            return GOOD_WORDS
    for b_word in BAD_WORDS:
        if re.search(b_word, question) != None:
            return BAD_WORDS
    return [""]

def find_company(question: str):
    company_name = []
    for key in stock_dict:
        for word in stock_dict[key]:
            if word in question:
                return key
    return "None"


def find_line(question: str, filename: str, words: List[str]):
    first_file = open(filename, "r")
    test1 = first_file.readlines()
    answers = []
    company_name = stock_dict[find_company(question)]
    for word in words:
        for name in company_name:
            for line in test1:
                if name in line:
                    x = re.search(word, line)
                    if x != None:
                        answers.append(line)
    first_file.close()
    answers = list(set(answers))
    return answers


def find_amt(company: str, line: str) -> str:
    match = ""
    for name in stock_dict[company]:
        if re.search(name, line) != None:
            match = re.search(name, line)
            numbers = re.findall("[0-9]+[.]+[0-9]+|[0-9]+[\s]*[0-9]*[/]+[0-9]*|[0-9]+[.]*[0-9]*[\s|.]+|[0-9]+[-]+point", line)
            if len(numbers) == 0:
                return "NA"
            elif len(numbers) == 1:
                return numbers[0]
            else:
                min_diff = 1000
                closest = ''
                for number in numbers:
                    test = abs(re.search(number, line).start() - match.start())
                    if test <= min_diff:
                        min_diff = test
                        closest = number
                return closest

def format_answers(question:str, filename: str):
    q_cat = question_cat(question)
    print(question+"\n")
    if q_cat == Q_type.INVALID:
        print("Invalid question, try again")
        return
    if q_cat == Q_type.HOW:
        words = []
        if q_open_or_close(question):
            words = ["[Oo]pen[ed]*", ["[Gg]round[ed]*"]]
        elif not q_open_or_close(question) and q_open_or_close(question) != None:
            words = ["[Cc]lose[ed]*"]
        else:
            words = q_inc_or_dec(question)
        lines = find_line(question, filename, words)
        i = 1
        if(lines == []):
            print("No answers found\n")
        else:
            for line in lines:
                if find_amt(find_company(question), line) != "NA":
                    print("A"+str(i)+": "+find_amt(find_company(question), line)+"\n")
                    print("Source: "+line)
                    i = i + 1
        return
    if q_cat == Q_type.WHAT:
        words = []
        if q_open_or_close(question):
            words = ["[Oo]pen[ed]*", "[Ff]inal"]
        elif not q_open_or_close(question):
            words = ["[Cc]lose[ed]*"]
        else:
            words = q_inc_or_dec(question)
        lines = find_line(question, filename, words)
        i = 1
        if(lines == []):
            print("No answers found\n")
        else:
            for line in lines:
                print("A"+str(i)+": "+find_amt(find_company(question), line)+"\n")
                print("Source: "+line)
                i = i + 1
        return
    if q_cat == Q_type.DID:
        all_words = GOOD_WORDS
        for b_word in BAD_WORDS:
            all_words.append(b_word)
        lines = find_line(question, filename, all_words)
        i = 1
        if(lines == []):
            print("No answers found\n")
        else:
            for line in lines:
                for word in all_words:
                    if re.search(word, line) != None: 
                        if(word in BAD_WORDS):
                            print("A"+str(i)+": It fell\n")
                            print("Source: " + line+"\n")
                            break
                        else:
                            print("A"+str(i)+": It rose\n")
                            print("Source: " + line+"\n")
                            break
                i = i + 1
        return

#how to run python main.py NAME_OF_FILE
def main():
    while(1):
        file = sys.argv[1]
        question = input("Ask your question here, say QUIT to quit\n")
        if question == "QUIT":
            break
        else:
            format_answers(question, file)
    print("Done!")


if __name__ == "__main__":
    main()
