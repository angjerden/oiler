__author__ = 'b543840'

num = dict()
num[0] = ''
num[1] = 'one'
num[2] = "two"
num[3] = "three"
num[4] = "four"
num[5] = "five"
num[6] = 'six'
num[7] = 'seven'
num[8] = 'eight'
num[9] = 'nine'
num[10] = 'ten'
num[11] = 'eleven'
num[12] = 'twelve'
num[13] = 'thirteen'
num[14] = 'fourteen'
num[15] = 'fifteen'
num[16] = 'sixteen'
num[17] = 'seventeen'
num[18] = 'eighteen'
num[19] = 'nineteen'
num[20] = 'twenty'
num[30] = 'thirty'
num[40] = 'forty'
num[50] = 'fifty'
num[60] = 'sixty'
num[70] = 'seventy'
num[80] = 'eighty'
num[90] = 'ninety'
num[100] = 'hundred'
num[1000] = 'thousand'

def spellNumber(n):
    returnString = ''
    n = str(n)
    if len(n) > 4:
        return returnString
    if len(n) > 3:
        returnString += spellThousand(int(n) / 1000)
    if len(n) > 2:
        returnString += spellHundred(str((int(n) / 100) % 10))
    teens = str(int(n) % 100)
    if len(n) > 1:
        tendigit = str((int(n) / 10) % 10)
        if returnString != '' and teens != '0':
            returnString += 'and'
        returnString += spellTen(tendigit)
    if int(teens) >= 10 and int(teens) < 20:
        returnString += num[int(teens)]
    else:
        returnString += num[int(n) % 10]

    return returnString

def spellThousand(t):
    if t != '0':
        return num[int(t)] + num[1000]
    else:
        return ''

def spellHundred(h):
    if h != '0':
        return num[int(h)] + num[100]
    else:
        return ''

def spellTen(t):
    if t != '0' and int(t) >= 2:
        return num[int(t)*10]
    else:
        return ''


length = 0
for i in range(1, 1001):
    spelled = spellNumber(i)
    print spelled
    length += len(spelled)

print "Length: " + str(length)
