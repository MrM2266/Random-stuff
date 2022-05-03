#34-Z5-2

def R(a):
    match a:
        case 1: return 5
        case 2: return 7
        case 3: return 6
        case 4: return 8
        case 5: return 3
        case 6: return 1
        case 7: return 4
        case 8: return 2

def L(a):
    match a:
        case 1: return 6
        case 2: return 8
        case 3: return 5
        case 4: return 7
        case 5: return 1
        case 6: return 3
        case 7: return 2
        case 8: return 4

def H(a):
    match a:
        case 1: return 4
        case 2: return 3
        case 3: return 2
        case 4: return 1
        case 5: return 7
        case 6: return 8
        case 7: return 5
        case 8: return 6

def V(a):
    match a:
        case 1: return 2
        case 2: return 1
        case 3: return 4
        case 4: return 3
        case 5: return 8
        case 6: return 7
        case 7: return 6
        case 8: return 5

def Rotate(operation, a):
    match operation:
        case "R": return R(a)
        case "L": return L(a)
        case "H": return H(a)
        case "V": return V(a)

def ProcessLine(line):
    znak = 1 #vždy rotujeme b
    for i in line:
        znak = Rotate(i, znak)

    return znak


def Show(znak):
    match znak:
        case 1: return "b"
        case 2: return "d"
        case 3: return "q"
        case 4: return "p"
        case _: return "?"

def GetInput():
    print("Enter/Paste data. Ctrl-D or Ctrl-Z (Win) to process.")
    data = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        data.append(line)

    return data


input = GetInput()

print("Output\n=======")
for line in input:
    print(Show(ProcessLine(line)))  