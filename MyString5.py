#***************************************************************
#Purpose:   Document your program
#
#
#***************************************************************
def printHeader (name, course, date):
    print("***************************************************************************")
    print("Name:\t", name)
    print("Course:\t", course)
    print("Date:\t", date)
    print("***************************************************************************")
#end of printHeader function

def scan(string):
    print("\n")
    print("1.\tOriginal string:", format(string, '>50s'))
    print("2.\tOriginal string length: ", format(len(string), '42d'))
    print("3.\tFirst character: ", format(string[0], '>49s'))
    print("4.\tLast character: ", format(string[len(string) - 1], '>50s'))
    print("5.\tMiddle character: ", format(string[(len(string)) // 2], '>48s'))
    print("6.\tOriginal string in swappedcase: ", format(string.swapcase(), '>34s'))
    print("7.\tOriginal string in lowercase: ", format(string.lower(), '>36s'))
    print("8.\tOriginal string in uppercase: ", format(string.upper(), '>36s'))
    print("9.\tOriginal string in title: ", format(string.title(), '>40s'))
    print("10.\tFirst word: ", format(string.split()[0], '>54s'))
    print("11.\tLast word: ", format(string.split()[-1], '>55s'))
    print("12.\tIs last word alphabet? ", format(str(string.split()[-1].isalpha()), '>43s'))
    print("13.\tAll 's' are replaced with '#?': ", format(string.replace("s", "#?"), '>34s'))
    print("14.\tLocate right most s in string: ", format(string.rfind("s"), '35d'))
    print("15.\tUnicode value for 1st character: ", format(ord(string[0]), '33d'))
#end of scan function  

#run functions
printHeader("Yasmeen Hart", "CS 1010", "9/21/2020")
scan("Valdosta State University")
scan("CS 1010 - Fall Semester, 20")
scan("Math 1111A Spring Semester")
