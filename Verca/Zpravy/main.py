#30-Z1-3

class CProcess:
    def __init__(self):
        self.data = {} # např. {"A":10, "B":5}

    def check(self, input):
        if (input in self.data): self.data[input] += 1 #pokud už písmeno v datech je, zvýší counter o 1
        else: self.data[input] = 1 #pokud tam není -> přidá písmeno do data

    def GetResult(self):
        return str(max(self.data, key = self.data.get)) #vrací písmeno s max výskytem a formátuje ho na string

    def Reset(self):
        self.data.clear() # vymaže dic data - pro použití s dlaší pozicí



#bere input - půjčeno z řešení
pocet_zprav, delka = map(int, input().split())
zpravy = [input() for _ in range(pocet_zprav)]


output = "" #definujeme si výstupní řetězec - aby bylo "k čemu přičítat"

core = CProcess() #instance třídy CProcess - má za úkol řešit jednu pozici za druhou

#prochází pozice ve všech zprávách - počítá si výskyty a sestavuje output
for i in range(0, delka): #zde by šlo ověřovat délku řetězců - první řádek inputu zcela zbytečný
    for zprava in zpravy:
        core.check(zprava[i])
    output += core.GetResult()
    core.Reset()

print(f"\nVysledny retezec:\n{output}")

#Hlavní omezení: pokud je výskyt stejný - bere prostě první nalezené písmeno - zadání neřeší tuto možnost - viz. demo.py