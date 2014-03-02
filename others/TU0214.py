# Det minste tallet som oppfyller disse betingelsene:
# Gir rest 17 hvis det deles med 18, rest 16 hvis det deles med 17
# helt ned til rest 1 hvis det deles med 2
import time
timer = time.time
t0 = timer()

for i in range(10000000, 1, -1):
    passed = True
    for div in range(18, 2, -1):
        #print "Sjekker divisjonen: " + str(i) + "%" + str(div) + " = " + str(i%div)
        if i % div != (div - 1):
            passed = False

    if passed == True:
        print str(i) + " oppfyller kravet."

print "Sekunder passert: " + str(timer() - t0)