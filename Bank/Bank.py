'''
Created on 15 sep 2013

@author: Kurtan
'''



class makeLoan:
    def __init__(self, P, r, a):
        self.P = P
        self.r = r
        self.a = a

    def calculateLoan(self):
        #raknar ut kostnaden for lanet, enligt given formel
        cost = self.P+(((self.a+1)*self.P*self.r)/2)
        return cost
        
def checkIfInt(i):
    try:
        int(i)
        return True
    except ValueError:
        return False
    
def checkIfFloat(f):
    try:
        float(f)
        return True
    except ValueError:
        return False
    
print "Programmet raknar nu ut kostnaden for ett lan"
print "Skriv in lanat belopp->"
amount = raw_input()
while(checkIfInt(amount) == False):
    print "Belopp maste vara ett heltal, forsok igen ->"
    amount = raw_input()

print "Skriv in den arliga rantesatsen->"
interestRate = raw_input()
while(checkIfFloat(interestRate) == False):
    print "Rantan maste vara ett heltal eller ett flyttal, forsok igen ->"
    interestRate = raw_input()

print "Skriv in antal ar->"
years = raw_input()
while(checkIfInt(years) == False):
    print "Antal ar maste vara ett heltal, forsok igen ->"
    years = raw_input()

loan = makeLoan(int(amount), float(interestRate), int(years))
print "Den totala kostnaden efter " + str(loan.a) + " ar ar " + str(loan.calculateLoan()) + "kr"








