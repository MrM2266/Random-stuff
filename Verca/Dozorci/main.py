#34-Z4-3
#requires python 3.10
class CDozorce: #třída pro jednoho dozorce - zná své souřadnice a směr, kam se dívá
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.hd = heading # < 1; > 2; A 3; V 4 =směr pohledu

    def GetNextHop(self): #levý horní roh má [x,y] = [0,0]
        #vrací souřadnice, kam by se měl pohybovat dál - neřeší zdi ani okraje desky
        match self.hd:
            case 1:
                return [self.x - 1, self.y]
            case 2:
                return [self.x + 1, self.y]
            case 3:
                return [self.x, self.y - 1]
            case 4:
                return [self.x, self.y + 1]
    
    def Go(self, x, y):
        #posune dozorce
        self.x = x
        self.y = y

    def Turn(self):
        #otočí dozorce z jeho pohledu doprava
        match self.hd:
            case 1:
                self.hd = 3
            case 2:
                self.hd = 4
            case 3:
                self.hd = 2
            case 4:
                self.hd = 1


class CZdi:
    def __init__(self):
        self.pozice = [] #list listů - obsahuje souřadnice všech zdí

    def AddZed(self, x, y):
        #přidá zeď do listu
        self.pozice.append([x, y])

    def GetZedStatus(self, x, y):
        #pokud na [x, y] není zed, vrací false; pokud tam je, vrací true
        if ([x, y] in self.pozice): return True
        else: return False

def LoadData(path):
    #načte data ze zadaného souboru a vrací je
    with open(path) as file: #bere si vstup ze souboru
        data = file.readlines()

    for i in range(0, len(data)):
        data[i] = data[i].rstrip("\n")

    data[0] = data[0].split(" ")
    return data

def VytvorObjekty(data, dozorci, zdi):
    #podle dat ze souboru si vytvoří objekty v paměti - dozorce a zdi
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            match data[i][j]:
                case "#": zdi.AddZed(j, i)
                case "<": dozorci.append(CDozorce(j, i, 1))
                case ">": dozorci.append(CDozorce(j, i, 2))
                case "A": dozorci.append(CDozorce(j, i, 3))
                case "V": dozorci.append(CDozorce(j, i, 4))

def Tah(zdi, dozorci, x_max, y_max):
    #provede jeden tah - posune, popř. otočí dozorce
    for dozorce in dozorci:
        next = dozorce.GetNextHop()
        if (next[0] >= x_max or next[0] < 0 or next[1] >= y_max or next[1] < 0):
            dozorce.Turn()
        elif (zdi.GetZedStatus(next[0], next[1])):
            dozorce.Turn()
        elif (not zdi.GetZedStatus(next[0], next[1])):
            dozorce.Go(next[0], next[1])

def Simuluj(zdi, dozorci, x_max, y_max, n):
    #provede n tahů
    for i in range(0, n):
        Tah(zdi, dozorci, x_max, y_max)

def GetMap(zdi, dozorci, x_max, y_max):
    #vrací grafickou mapu - je to list str - každý str je jeden řádek
    output = []
    map = [None] * y_max

    for i in range(0, len(map)):
        map[i] = [None] * x_max

    for zed in zdi.pozice:
        map[zed[1]][zed[0]] = "#"

    for dozorce in dozorci:
        match dozorce.hd:
            case 1: map[dozorce.y][dozorce.x] = "<"
            case 2: map[dozorce.y][dozorce.x] = ">"
            case 3: map[dozorce.y][dozorce.x] = "A"
            case 4: map[dozorce.y][dozorce.x] = "V"

    for i in range(0, len(map)):
        pom = ""
        for j in range(0, len(map[i])):
            if (map[i][j] == None): map[i][j] = "."
            pom += map[i][j]
        output.append(pom)

    return output



data = LoadData("data.txt")
pocetKroku = int(data[0][2]) #od pythonu 3 de facto int nemá hranici (viz. interpreter's word size)
del data[0]

x_max = len(data[0]) #rozmer hraci plochy - max hodnoty souradnic pro dozorce
y_max = len(data)

zdi = CZdi()
dozorci = []
VytvorObjekty(data, dozorci, zdi)

Simuluj(zdi, dozorci, x_max, y_max, pocetKroku)

map = GetMap(zdi, dozorci, x_max, y_max)

for i in map: #zobrazí mapu
    print(i)

#program neřeší, když jsou ve výsledku "na sobě" dva dozorci - jejich směry se přepíší