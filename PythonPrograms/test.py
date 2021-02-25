


a = 'hello'
b = ''
p = 3
q = 11
e = 9

for l in a:
    print l + " : " + str((ord(l)-96))


print ""

for l in a:
    print l + " : " + str((ord(l)-96)**e % (p * q))
