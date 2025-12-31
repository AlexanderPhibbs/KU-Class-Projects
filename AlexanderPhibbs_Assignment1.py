'''
Name: Alexander Phibbs
Date: 1/25/2024
Program: EECS210Project1.py
Description: Python program going through Demorgans first and second laws with the associative laws and two
test cases.
This project was Coded by Alexander Phibbs.
'''
def Main():#this runs the main body of the Program
    Demorgans1()#these next 6 are the laws and test case programs that will be defined later
    Demorgans2()
    AssociativeLaw1()
    AssociativeLaw2()
    Casenum5()
    Casenum6()

def Demorgans1():#this goes through the logic if Demorgans First Law
    print("1) DeMorgans First Law")#This prints the header
    print("p \t\t q \t\t !(p*q)\t !p+!q")#this prints the columns headers
    print(f"True \t True \t {not(True and True)} \t {not(True) or not(True)}")#This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t {not (True and False)} \t {not(True) or not(False)}") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t {not (False and True)} \t {(not(False)) or (not(True))}") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t {not (False and False)} \t {(not(False)) or (not(False))}") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print('\n') #this adds a new line to space out the print statements

def Demorgans2():#this goes through the logic of Demorgans First Law
    print("2) DeMorgans Second Law")#this print the header for demorgans second law
    print("p \t\t q \t\t !(p+q)\t !p*!q")#this line prints the column headers
    print(f"True \t True \t {not (True or True)} \t {not(True) and not(True)} ") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t {not (True or False)} \t {not(True) and not(False)} ") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t {not (False or True)} \t {(not(False)) and(not(True))} ") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t {not (False or False)} \t {(not(False)) and (not(False))} ") #This sets up the booleen variables and
    #uses logic operators to show which values are true and false in the tables
    print('\n')

def AssociativeLaw1():#this goes through the logic of  the first associative law
    print("3) Associative Law 1")#this print a header
    print("p \t\t q \t\t r \t\t (p*q)*r \t p*(q*r)")#this prints the columns for the associative law
    print(f"True \t True \t True \t {(True and True) and True} \t\t {True and (True and True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t True \t False \t {(True and True) and False} \t\t {True and (True and False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t True \t {(True and False) and True} \t\t {True and (False and True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t False \t {(True and False) and False} \t\t {True and (False and False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t True \t {(False and True) and True} \t\t {False and (True and True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t False \t {(False and True) and False} \t\t {False and (True and False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t True \t {(False and False) and True} \t\t {False and (False and True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t False \t {(False and False) and False} \t\t {False and (False and False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print('\n')

def AssociativeLaw2():
    print("4) Associative Law 2")
    print("p \t\t q \t\t r \t\t (p+q)+r \t p+(q+r)")
    print(f"True \t True \t True \t {(True or True) or True} \t\t {True or (True or True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t True \t False \t {(True or True) or False} \t\t {True or (True or False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t True \t {(True or False) or True} \t\t {True or (False or True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t False \t {(True or False) or False} \t\t {True or (False or False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t True \t {(False or True) or True} \t\t {False or (True or True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t False \t {(False or True) or False} \t\t {False or (True or False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t True \t {(False or False) or True} \t\t {False or (False or True)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t False \t {(False or False) or False} \t\t {False or (False or False)} ")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print('\n')

def Casenum5():
    print("5) ((p+q)*(p->r)*(q->r)->r=T")
    print("p \t\t q \t\t r \t\t ((p+q)*(p->r)*(q->r)->r \t T")
    print(f"True \t True \t True \t {Implication((True or True) and Implication(True,True)and Implication(True,True),True)} \t\t\t\t\t\t True ")
    #This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    #be true for the second value entered or all of the first values will be false
    print(f"True \t True \t False \t {Implication((True or True) and Implication(True,False)and Implication(True,False),False)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print(f"True \t False \t True \t {Implication((True or False) and Implication(True,True)and Implication(False,True),True)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print(f"True \t False \t False \t {Implication((True or False) and Implication(True,False)and Implication(False,False),False)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print(f"False \t True \t True \t {Implication((False or True) and Implication(False,True)and Implication(True,True),True)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print(f"False \t True \t False \t {Implication((False or True) and Implication(False,False)and Implication(True,False),False)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print(f"False \t False \t True \t {Implication((False or False) and Implication(False,True)and Implication(False,True),True)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print(f"False \t False \t False \t {Implication((False or False) and Implication(False,False)and Implication(False,False),False)} \t\t\t\t\t\t True ")
    # This loops the implications together to eventually make everything true, this is done with showing that in some way one of these values will
    # be true for the second value entered or all of the first values will be false
    print('\n')

def Implication(p,q):#This goes through the implication logic and allows for you to pass two variables
    if q == True:#if the q or the variable being compared to is true then its automatically true
        return True
    elif p == False:#if the first variable is false then the statement is automatically true
        return True
    else:
        return False#everything else is false
def Biconditional(q,p):#This handles the two variable bicondition
    if q == p:#This goes through the boolean logic to allow for a biconditional arguments to be handled
        return True
    elif p != q:#if p is not q then the biconditional logic says this statement cannot be true
        return False

def Casenum6():
    print("6) (p<->q)=(p->q)*(q->p)")
    print("p \t\t q \t\t (p<->q)\t (p->q)*(q->p)")  # this prints the columns headers
    print(f"True \t True \t {Biconditional(True,True)} \t\t {Implication(True,True) and Implication(True,True)}")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"True \t False \t {Biconditional(False,True)} \t\t {Implication(True,False) and Implication(False,True)}")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t True \t {Biconditional(True,False)} \t\t {Implication(False,True) and Implication(True,False)}")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print(f"False \t False \t {Biconditional(False,False)} \t\t {Implication(False,False) and Implication(False,False)}")
    # This sets up the booleen variables and uses logic operators to show which values are true and false in the tables
    print('\n')  # this adds a new line to space out the print statements

if __name__=='__main__':
    Main()