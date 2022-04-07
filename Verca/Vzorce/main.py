#34-Z3-3
import re

class Core:
    def __init__(self):
        self.result = []
        self.process = []
        self.vzorce = {}
        self.veliciny = []
        self.vzorceRaw = []

    def ParseVzorce(self, data):
        #ze stringu udělá dic vzorců
        self.vzorceRaw = data.copy() #uloží si vzorce pro zobrazení (pro tvar y = a + b)

        for i in range(0, len(data)):
            data[i] = data[i].replace("=", "")
            data[i] = data[i].split("  ")
            if data[i][0] in self.vzorce:
                pom = self.vzorce[data[i][0]]
                self.vzorce[data[i][0]] = [pom, data[i][1]]
            else:
                self.vzorce[data[i][0]] = data[i][1]

    def ParseVeliciny(self, data):
        #uloží si počáteční veličiny
        self.veliciny = data.split(" ")

    def NajdiVzorec(self, x):
        #najde vzorec pro x
        if (type(self.vzorce[x]) is list):
            #musí zabránit tomu, aby se při řešení fn řešilo znovu fn -> infinite loop
            #najde si výrazy pro x; projde je a podívá se, jestli existuje nějaký, který neobsahuje nic z process - ten použije
            for vzorec in self.vzorce[x]:
                found = 0
                cleny = self.GetCleny(vzorec)
                for clen in cleny:
                    if (clen in self.process): found = 1

                if (found == 0): return vzorec

        else: return self.vzorce[x]

    def GetCleny(self, x):
        #vrací list clenu ve výrazu x
        x = x.replace(" ", "")
        x = re.split("\+|-|\*|/", x)
        return x

    def Solve(self, x):
        # x je řešený výraz
        #podívám se na fci - najdu si v ní členy - ty porovnám s velicinami - pokud to:
        #není veličina - hledám vzorec pro neznámou
        #je veličina - ignoruji - je solved
        #jakmile mám oba členy solved - vracím pole stringů - hotových vzorců
        if (x not in self.result):
            self.result.append(x)

        x = self.GetCleny(x)

        for clen in x:
            if clen not in self.veliciny:
                self.process.append(clen)
                self.Solve(self.NajdiVzorec(clen))
                self.veliciny.append(clen)
                self.process.remove(clen)

    def GetOutput(self):
        output = []
        for res in self.result:
            for vzorec in self.vzorceRaw:
                if (res in vzorec):
                    output.append(vzorec)
        output.reverse()
        return output

    def FindSolution(self, var):
        if (var not in self.process):
            self.process.append(var)

        self.Solve(self.NajdiVzorec(var))
            



with open("data.txt") as file: #bere si vstup ze souboru
    data = file.readlines()

for i in range(0, len(data)):
    data[i] = data[i].rstrip("\n")

data[0] = data[0].split(" ")

cil = data[0][2]
velicinyRaw = data[1]
del data[0:2]


core = Core()
core.ParseVzorce(data)
core.ParseVeliciny(velicinyRaw)

core.FindSolution(cil)

for res in core.GetOutput():
    print(res)

#není úplně dořešené, co dělat, když je více možných řešení