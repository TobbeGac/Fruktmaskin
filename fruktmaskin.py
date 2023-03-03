import random
#Visar hur man använder funktioner för att samla och återanvända kod

#skapa array med tuple
frukter = ("Apelsin", "Banan", "Melon", "Kiwi", "Citron")
looping = True

#Definierar funktion
def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer Här!\n")

#Huvud program
print("\n-:Fruktmaskin:-\n")


while looping:

    i = 1
    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1

    fruktnr = input("\nMata in nr på frukt du vill ha: ")
    print_fruit(fruktnr)
    
    go = input("\nVill du ha en frukt till ")

    if (go == "n"):
        break

print("------------------------------------------------------------------------------------------------------------------")

print("\nFöresten, du får en frukt till för du 'r snäll!\n")
slumpfrukt = random.randint(1, 5)
print_fruit(slumpfrukt)

