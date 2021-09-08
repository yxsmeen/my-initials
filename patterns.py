#**********************************************************
#Purpose: Display number patterns as designated by user
#
#Input: Number to display the pattern of
#
#Output: Different number arrangments
#
#Course:    D o c u m m e n t your program and functions
#
#Author: Yasmeen Hart
#
#Date: Oct 12, 2020
#
#Course: CS 1010
#*********************************************************

#patternI displays the following pattern

##   1 
##   1 2 
##   1 2 3 
##   1 2 3 4 
##   1 2 3 4 5 
##   1 2 3 4 5 6
##
##
def pattern1(n):
    print("\n\tPattern I")
    for i in range (1, n+1, 1):
        print()
        for j in range (1, i+1, 1):
            print (j, end = ' ')
        #End of inner loop
    #End of outer loop
    
    
#End of patternI
            
#patternII displays the following pattern
    
    
##   1 2 3 4 5 6 
##   1 2 3 4 5 
##   1 2 3 4 
##   1 2 3 
##   1 2 
##   1 
##
def pattern2(n):
    print("\n\tPattern II")
    for i in range (n, 0, -1):
        print()
        for j in range (1, i + 1, 1):
            print(j, end = ' ')
        #end of inner loop
    #end of outer loop
    print()
#End of PatternII
    

##patternIII displays the following pattern                            

##   
##             6 
##           5 6 
##         4 5 6 
##       3 4 5 6 
##     2 3 4 5 6 
##   1 2 3 4 5 6 
##

def pattern3 (n):
    print ("\n\tPattern III")
    for i in range(1, n + 1):
        print()
        for j in range (1, n + 1):
            if(j <= n - i):
                print(' ', end = ' ')
            else:
                print(j, end = ' ')
        #end of inner loop
    #end of outer loop
    print()
#End of patternIII

#patternIV displays the following pattern
##   
##   1 2 3 4 5 6 
##     2 3 4 5 6 
##       3 4 5 6 
##         4 5 6 
##           5 6 
##             6 
##   
def pattern4(n):
    print ("\n\n\tPattern IV")
    for i in range (1, n + 1):
        print()
        for j in range (1, n + 1):
            if(j < i):
                print(' ', end = ' ')
            else:
                print(j, end = ' ')
        #end of inner loop
    #end of outer loop
    print()
#End of patternIV

#patternV displays the following pattern
##   
##   1 2 3 4 5 6 5 4 3 2 1     
##     2 3 4 5 6 5 4 3 2              
##       3 4 5 6 5 4 3
##         4 5 6 5 4
##           5 6 5 
##             6
           
def pattern5(n):
    print ("\n\n\tPattern V")
    for i in range (1, n + 1, 1):
        print()
        for t in range (1, 1 + i, 1):
            print(' ', end = ' ')
        for j in range (i, n + 1, 1):
            print(j, end = ' ')
        for k in range (n - 1, i - 1, -1):
            print(k, end = ' ')
        #end of inner loop
    #end of outer loop
    print()
#End of patternV
            
#patternVI displays your own pattern
##   
##   1 2 3 4 5 6     
##     2 3 4 5 6             
##       3 4 5 6 
##         4 5 6 
##           5 6 
##             6
##           5 6           
##         4 5 6 
##       3 4 5 6 
##     2 3 4 5 6 
##   1 2 3 4 5 6 
##   
##   
##
            
def pattern6(n):
    print("\n\n\tMy Own Pattern")8
    for i in range (1, n + 1, 1):
        print()
        for k in range (1, i, 1):
            print(' ', end = ' ')
        for j in range (i, n + 1, 1):
            print(j, end = ' ')
        #end of inner loop
    #end of outer loop
    for i in range (n - 1, 0, -1):
        print()
        for k in range (1, i, 1):
            print(' ', end = ' ')
        for j in range (i, n + 1, 1):
            print(j, end = ' ')
        #end of inner loop
    #end of outer loop
    print()
#End of patternVI

