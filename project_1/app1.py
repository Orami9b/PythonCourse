import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    output = ""
    if word in data.keys():
        output = data[word]
    elif word.capitalize() in data.keys():
        output = data[word.capitalize()]
    elif word.upper() in data.keys():
        output = data[word.upper()]
    else:
        lst = get_close_matches(word, data.keys(), cutoff = .8)
        if lst:
            response = input("Did you mean '%s' instead? Enter Y if yes or N for no: " % lst[0])
            if response.upper() == "Y":
                output = data[lst[0]]
            elif response.upper() != "N":
                output = "You did not enter Y or N."
    if output == "":
        output = "The word is not in the dictionary."

    return output

def displayTranslation(translatedWord):
    if type(translatedWord) == list:
        for string in translatedWord:
            print(string)
    else:
        print(translatedWord)

word = input("Enter a word: ")
displayTranslation(translate(word))