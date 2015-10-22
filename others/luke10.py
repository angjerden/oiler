#
# Velkommen til Knowit sitt julebord!
#
# På julebordet er vi 1500 mennesker som sitter rundt et stort bord.
# Vi er nummerert fra 1 til 1500 langs bordet.
# Vi har fått tak i en flaske med meget sterk (men god!) akevitt.
#
# Den første personen tar flasken og serverer person nummer to en dram.
# Akevitten er så sterk at denne personen går rett i bakken.
# Person nummer en sender så flaska videre til den tredje personen
# som serverer den fjerde en dram. Han går også rett i bakken
# og flasken sendes videre til femtemann. Dette fortsetter rundt
# slik at person nummer 1499 serverer person 1500 en dram
# (hvorpå han dundrer i gulvet) og gir flaska tilbake den første.
#
# Nå serverer den første personen den tredje (som deiser av stolen)
# og gir flaska videre til den femte...
#
# Dette fortsetter til det bare er en person igjen.
# Hvilken person sitter igjen ved julebordets slutt?
#
# Svaret skal være i form av nummeret på personen som
# sitter igjen, eksempelvis 1337
#

min = 1
max = 1500 + 1

sober = "0"
drunk = "X"

people = dict((i, sober) for i in range(min, max))
number_sober = len(people.keys())

def serveAquavitToTheNextGuy(input):
    global number_sober
    index = input + 1
    while index != input:
        if index in people and people[index] != drunk:
            people[index] = drunk
            print("{} got served by {} and is drunk".format(index, input))
            number_sober -= 1
            break
        index = index + 1
        if index >= max:
            index = min


def printVictor():
    for i in range(min, max):
        if people[i] == sober:
            print("{} is still sober!".format(i))

if __name__ == "__main__":
    i = min
    while number_sober > 1:
        if people[i] != drunk:
            print("{} receives bottle".format(i))
            serveAquavitToTheNextGuy(i)
        else:
            pass
            #print("{} is already drunk. Moving on...".format(i))
        i += 1
        if i >= max:
            i = min
    print("\n{} sober person left".format(number_sober))
    printVictor()
