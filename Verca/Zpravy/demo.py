test = {"M":3, "B":100, "C":100}


print(max(test, key= test.get))

# B i C mají stejný výskyt (100) -> fce max vrátí B - je první v dic
# vrátí vždy první výskyt - neřeší -> limit programu