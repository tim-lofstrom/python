


def telbook():

    dic = {}

    while True:
        i = raw_input("telbook>").split()
        if len(i) == 3 and i[0] == "add":
            if add(dic, i[1], i[2]):
                print "added", i[1], "with number", i[2]
            else:
                print i[1], "already exists"
        elif len(i) == 2 and i[0] == "lookup":
            num = lookup(dic, i[1])
            if num:
                print i[1], "has number", num[0]
            else:
                print "not found"
            
        elif len(i) == 3 and i[0] == "alias":
            if alias(dic, i[1], i[2]):
                print i[1], "now has alias", i[2]
            else:
                print "not found"
                
        elif len(i) == 3 and i[0] == "change":
            if change(dic, i[1], i[2]):
                print "changed",i[1], "to", i[2]
            else:
                print "not found"
                
        elif len(i) == 2 and i[0] == "load":
            if load(dic, i[1]):
                print "loaded from", i[1], "successfully"
        elif len(i) == 2 and i[0] == "save":
            if save(dic, i[1]):
                print "saved to file", i[1]
        elif len(i) == 1 and i[0] == "quit":
            print "Terminating telbook."
            return
        
def add(dic, name, num):
    if not lookup(dic,name):
        dic[name] = [num]
        return True

def lookup(dic, name):
    if name in dic:
        return dic[name]

def alias(dic, name, newname):
    if name in dic:
        dic[newname] = dic[name]
        return True

def change(dic, name, newnum):
    if name in dic:
        dic[name][0] = newnum
        return True

def load(dic, filename):
    try:
        f = open(filename, "r")
        dic.clear()
        for line in f:
            i = line.split(";")
            add(dic, i[0], i[1])
        f.close()
    except IOError:
        print "error opening file", filename
        return False
    return True
            

def save(dic, filename):
    try:
        f = open(filename, "w")
        for name, num in dic.iteritems():
            f.write(name + ";" + num[0]+";\n")
        f.close()
    except IOError:
        print "error saving to file", filename
        return False
    return True


telbook()
