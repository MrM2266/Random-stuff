<<<<<<< HEAD
#34-Z1-2

import datetime

def Parser(input):
    #pro načtení dat do objektu datetime -> snadno se řadí
    input = input.split(" ")

    date = input[0]
    time = input[1]

    date = date.split("-")
    time = time.split(":")

    out = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
    print(out)

    return out


def GetSortedIndexes(input):
    dates = []

    for i in input:
        dates.append(Parser(i))

    indexes = sorted(range(len(dates)), key=lambda k: dates[k])
    output = [None] * len(indexes)

    for i in indexes:
        output[indexes[i]] = i + 1

    return output


pocet = int(input())
input_raw = [input() for _ in range(pocet)]


vysledky = GetSortedIndexes(input_raw)

for s in range(0, len(vysledky)):
    print(f"{input_raw[s]}    {vysledky[s]}")



#na prvním místě by bylo to, co má index 2 -> jednička musí být na 2. (resp. na třetí) pozici
#dvojka musí být na nulté (první) pozici
=======
#34-Z1-2

import datetime

def Parser(input):
    #pro načtení dat do objektu datetime -> snadno se řadí
    input = input.split(" ")

    date = input[0]
    time = input[1]

    date = date.split("-")
    time = time.split(":")

    return datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))

def GetSortedIndexes(input):
    dates = []

    for i in input:
        dates.append(Parser(i))

    indexes = sorted(range(len(dates)), key=lambda k: dates[k])
    output = [None] * len(indexes)

    for i in indexes:
        output[indexes[i]] = i + 1

    return output


pocet = int(input())
input_raw = [input() for _ in range(pocet)]


vysledky = GetSortedIndexes(input_raw)

for s in range(0, len(vysledky)):
    print(f"{input_raw[s]}    {vysledky[s]}")



#na prvním místě by bylo to, co má index 2 -> jednička musí být na 2. (resp. na třetí) pozici
#dvojka musí být na nulté (první) pozici
>>>>>>> 74c49f558ae5a4b9ef42cf25a9fbf0ddd04a06ac
#indexes: [2, 0, 3, 1]