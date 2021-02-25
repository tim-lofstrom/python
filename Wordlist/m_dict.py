'''
Created on 30 sep 2013

@author: Kurtan
'''
import Wordlist

def main_dict():
    
    dic = {} #initialize an empty dictionary

    while True:
        Wordlist.printMenu()
        alt = Wordlist.getInput() #getInput makes sure the input is correct
        
        #test alt to see which function to execute
        if(alt == 1): #enter new word
            w = raw_input("Enter word ->")
            if(Wordlist.lookupItem(w, dic) != None):
                Wordlist.printError(1) #print error code 1, word already exist
            else:
                d = raw_input("Enter description ->")
                Wordlist.addItem(w, d, dic)
            
        elif(alt == 2): #lookup word
            s = raw_input("Search for ->")
            result = Wordlist.lookupItem(s, dic)
            if(result != None):
                Wordlist.displayResult(result)
            else:
                Wordlist.printError(2) #print error code 2, word do not exist
                
        elif(alt == 3): #delete word
            d = raw_input("Delete word ->")
            if(Wordlist.deleteItem(d, dic) == True):
                print "Word deleted"
            else:
                Wordlist.printError(2) #print error code 2, word do not exist
                
        elif(alt == 4): #traverse
            Wordlist.traverse(dic)
        elif(alt == 5): #exit program
            break
        
main_dict()


