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



input = ["2020-05-15 10:26:57",
"2020-05-18 17:32:00",
"2020-04-30 22:11:53",
"2020-05-18 16:20:15"]



vysledky = GetSortedIndexes(input)

for s in range(0, len(vysledky)):
    print(f"{input[s]}    {vysledky[s]}")



#na prvním místě by bylo to, co má index 2 -> jednička musí být na 2. (resp. na třetí) pozici
#dvojka musí být na nulté (první) pozici
#indexes: [2, 0, 3, 1]