#*********************************************************
#
#   Program: 
#       Basic Finite State Machine
#
#   Programmer: 
#        Austin Oakes
#
#   Description:
#       This program was created in order to learn
#   the basics of a finite state machine. It will
#   take a list of bits (1 or 0) and check to seek
#   if the list ended with two or more 0's in a row. 
#   "Yes" will be printed if it passed and "No" if the 
#   test failed.
#
#   Test Pass ex. [1, 0, 0, 0] 
#
#*********************************************************

#Program starting state. Only entered once.
def StartState(bits):

    #if the list was empty to start with, it failed.
    if bits == []:
        print("No")
        return []

    #If the first element was 0, got to zero state.
    if bits[0] == 0:
        BitIsZero(bits[1:])
        
    #Otherwise go the 1 state.
    else:
        BitIsOne(bits[1:])

#This state is entered when the previous number was 1
#Test fails if the list is empty.
def BitIsOne(bits):

    #If list is empty, the test did not pass.
    if bits == []:
        print("No")
        return []

    #If the first element was 0, got to zero state.
    if bits[0] == 0:
        BitIsZero(bits[1:])

    #Otherwise go the 1 state.
    else:
        BitIsOne(bits[1:])

#This state is entered when the previous number was 0
#for the first time. Test fails if the list is empty.
def BitIsZero(bits):

    #If list is empty, the test did not pass.
    if bits == []:  
        print("No")
        return []

    #If the first element was 0, go to ZeroAgain state.
    if bits[0] == 0:
        BitIsZeroAgain(bits[1:])

    #Otherwise assume it was 1, and go to OneState.
    else: 
        BitIsOne(bits[1:])

#This state is entered when 0 was the previous 
#number in the list, two or more times in a row.
#If the list is empty, then that bit string test passed.
def BitIsZeroAgain(bits):
    
    #If the list is empty, the test passed.
    if bits == []:  
        print("Yes")
        return []

    #If the first element was 0 once again, stay in this state.
    if bits[0] == 0:
        BitIsZeroAgain(bits[1:])
        
    #Otherwise assume it was 1, and go to OneState.
    else: 
        BitIsOne(bits[1:])

#***    Test Cases     ***

StartState([0, 1, 1, 0, 1])                             #NO
StartState([1, 1, 0, 0])                                #YES
StartState([1, 0, 1, 0, 1, 1, 0, 0, 0])                 #YES
StartState([0, 0, 0, 1, 0])                             #NO
StartState([0, 0])                                      #YES
StartState([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])     #NO
StartState([1, 1])                                      #NO
StartState([])                                          #NO
StartState([0])                                         #NO
StartState([1])                                         #NO
