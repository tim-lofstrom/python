'''
Created on 30 sep 2013

@author: Kurtan
'''

import Wordlist

def main_tuple(): #main function for the tuple list
    
    items = [] #initialize an empty list, wich will contain the tuples

    while True:
        Wordlist.printMenu()
        alt = Wordlist.getInput() #getInput makes sure the input is correct
        
        #test alt to see which function to execute
        if(alt == 1): #enter new word
            w = raw_input("Enter word ->")
            if(Wordlist.lookupItem(w, items) != None):
                Wordlist.printError(1) #print error code 1, word already exist
            else:
                d = raw_input("Enter description ->")
                Wordlist.addItem(w, d, items)
            
        elif(alt == 2): #lookup word
            s = raw_input("Search for ->")
            result = Wordlist.lookupItem(s, items)
            if(result != None):
                Wordlist.displayResult(result)
            else:
                Wordlist.printError(2) #print error code 2, word do not exist
            
        elif(alt == 3): #delete word
            d = raw_input("Word to delete ->")
            if(Wordlist.deleteItem(d, items) == True):
                print "Word deleted"
            else:
                Wordlist.printError(2) #print error code 2, word do not exist
                
        elif(alt == 4): #traverse
            Wordlist.traverse(items)
        elif(alt == 5): #exit program
            break
        
main_tuple()


