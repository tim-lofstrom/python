'''
Created on 28 sep 2013

@author: Kurtan
'''

def printMenu(): #general function for a menu
    print "----------------------"
    print "Main menu:"
    print ""
    print "1. Insert"
    print "2. Lookup"
    print "3. Delete"
    print "4. Traverse"
    print "5. Exit program"  

def checkIfInt(i): #Check if really an int and handle value error
    try:
        int(i)
        return True
    except ValueError:
        return False
    
def getInput(): #get input from user to navigate menu, input must be valid
    while True:
        alt = raw_input("->")
        while((checkIfInt(alt) == False) or ((int(alt) < 1) or (int(alt) > 5)) == True): #while the input is not valid
            printError(3) #print error code 3, invalid menu input
            printMenu()
            alt = raw_input("->")
        return int(alt) #when an valid input is written, return
    
def addItem(w, d, *args): #word, description and the list
    if(len(args) == 2): #It is two string lists
        args[0].append(w)
        args[1].append(d)
    elif(type(args[0]) == list): #it is a list of tuples
        t = (w, d)
        args[0].append(t)
    elif(type(args[0]) == dict): #it is a dictionary
        args[0][w] = d
    
def lookupItem(s, *args):#word to search for and the list
    if(len(args) == 2): #It is two string lists
        index = 0
        for i in args[0]:
            if(i == s):
                return i, args[1][index] #result found, return it
            index += 1
    elif(type(args[0]) == list): #it is a list of tuples
        index = 0
        for i in args[0]:
            if(i[0] == s):
                return i[0], args[0][index][1] #result found, return it
            index += 1
    elif(type(args[0]) == dict): #it is a dictionary
        for i, j in args[0].iteritems():
            if(i == s):
                return i, j #result found, return it
    
def deleteItem(d, *args): #word to delete and the list
    if(len(args) == 2): #It is two string lists
        index = 0
        for i in args[0]:
            if(i == d):
                args[0].pop(index) #result found, delete it and return true
                args[1].pop(index)
                return True
            index += 1
    elif(type(args[0]) == list): #it is a list of tuples
        index = 0
        for i in args[0]:
            if(i[0] == d):
                args[0].pop(index) #result found, delete it and return true
                return True
            index += 1
    elif(type(args[0]) == dict): 
        for i, j in args[0].iteritems(): 
            if(i == d):
                del args[0][d] #result found, delete it and return true
                return True

def traverse(*args): # print all items in the list
    print args[0]
        
def printError(errorCode): #general function for displaying error messages by given code
    if(errorCode == 1):
        print "Word already exists"
    elif(errorCode == 2):
        print "Word can not be found"
    elif(errorCode == 3):
        print "Invalid menu input"
    
def displayResult(res): #function for displaying a result, the word and its description
    print "Word: " + str(res[0]) + " Description: " + str(res[1])







