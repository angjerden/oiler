__author__ = 'b543840'

h = 3
w = 3
mark = "X"
right = '>'
down = 'v'
route_count = 0

def printLattice(lattice):
    output = ""
    for i in range(0, len(lattice)):
        for j in range(0, len(lattice[i])):
            output += "[" + lattice[i][j] + "]"
        output += "\n"
    print output + "\n\n"

def initLattice(lattice):
    for i in range(0, h):
        lattice.append([])
        for j in range(0, w):
            lattice[i].append('-')

def resetLattice(lattice):
    for i in range(0, h):
        if lattice[i][1] != mark:
            for j in range(0, w):
                lattice[i][j] = '-'

def setCell(lattice, i, j, content):
    if lattice[i][j] != mark:
        lattice[i][j] = content


if __name__ == "__main__":
    lattice = []

    initLattice(lattice)
    printLattice(lattice)

    i = 0
    j = 0
    w_frame = w  # used when an entire column is marked, it shrinks the 'frame' in which j can move
    stop = False

    while not stop:
        while i < len(lattice) - 1 or j < len(lattice[i]) - 1:
            if j + 1 < w_frame and lattice[i][j + 1] != mark:
                setCell(lattice, i, j, right)
                j += 1
            elif j + 1 == w_frame:
                lattice[i][j] = mark
                route_count += 1
                if i + 1 == len(lattice) - 1:
                    w_frame -= 1
                while i < len(lattice) - 1:
                    setCell(lattice, i, j, down)
                    i += 1
            elif lattice[i][j + 1] == mark:
                i += 1
            printLattice(lattice)
        resetLattice(lattice)
        i = j = 0
        if route_count >= 6:
            stop = True
print "Route count: " + str(route_count)

'''

    Hvis kolonne + 1 ikke er lik lengden av array og ikke inneholder 'X'
        Gaa til hoyre (kolonne + 1)
    Ellers, hvis kolonne + 1 inneholder 'X'
        Gaa 1 ned (rad + 1)
    Ellers, Hvis kolonne + 1 er lik lengden av array (at man moeter 'veggen')
        Sett x paa punktet du er paa
        Gaa nedover til maal (rad ++ til i og j er lik sine respektive maksstoerrelser - 1)

'''