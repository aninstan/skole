x = int(input("Skriv inn et heltall: "))
nr = []

while len(nr) < 9:
    if x in nr:
        print("Tallet", x, "finnes allerede i listen")
        x = int(input("Skriv inn et heltall: "))
    else:
        nr.append(x)
        x = int(input("Skriv inn et heltall: "))

print(nr)