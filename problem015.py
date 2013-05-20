__author__ = 'b543840'

h = 9
w = 9

def printLattice(lattice):
    output = ""
    for i in range(0, len(lattice)):
        for j in range(0, len(lattice[i])):
            output += "[" + str(lattice[i][j]) + "]"
        output += "\n"
    print output + "\n"

def initLattice(lattice):
    for i in range(0, h):
        lattice.append([])
        for j in range(0, w):
            lattice[i].append(1)


if __name__ == "__main__":
    lattice = []

    initLattice(lattice)
    printLattice(lattice)


    for i in range(1, h ):
        for j in range(1, w):
            lattice[i][j] = lattice[i - 1][j] + lattice[i][j - 1]

    printLattice(lattice)

