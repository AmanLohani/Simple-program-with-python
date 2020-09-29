import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0:
        print("Did you mean %s word" %get_close_matches(word , data.keys()) [0])
        decide = input("Enter y for yes and n for no")
        if decide == 'y':
            return(data[get_close_matches(word , data.keys())[0]])
        elif decide == 'n':
            print("Word not found")
        else:
            print("Enter y or n")
    else:
        print("Word not found")


word = input("enter the word")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)





