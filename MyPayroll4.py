#****************************************
#Purpose: Create a payroll
#           
#
#
#Input:
#
#Output:
#               
#Course: CS 1010
#
#Author:Yasmeen Hart
#
#Date: Sept 21, 2020
#
#****************************************
#

def computePay (hours, hourlyRate):
    if(hours <= 40):
        regularPay = hours * hourlyRate
        overtimePay = 0
    else:
        regularPay = 40 * hourlyRate
        overtimePay = (hours - 40) * hourlyRate * 1.5
    grossPay = regularPay + overtimePay
    return regularPay, overtimePay, grossPay
#End of computePay

def computeTaxes (grossPay, stateRate, federalRate, FICA_rate):
    stateTax = grossPay * stateRate
    federalTax = grossPay * federalRate
    FICA_tax = grossPay * FICA_rate
    totalDeduction = stateTax + federalTax + FICA_tax
    netPay = grossPay - totalDeduction
    return stateTax, federalTax, FICA_tax, totalDeduction, netPay
#End of computeTaxes


def printAll (name, company, hours, hourlyRate,stateRate,federalRate,
              FICA_rate, stateTax, federalTax,FICA_tax, regularPay,
              overtimePay, grossPay,totalDeduction, netPay):
    print("Name:            ", name)
    print("Company:         ", company)
    print("Hours:           ", hours)
    print("Hourly Rate:     ", hourlyRate)
    print("State Rate:      ", stateRate)
    print("Federal Rate:    ", federalRate)
    print("FICA Rate:       ", FICA_rate)
    print("State Tax:       ", stateTax)
    print("Federal Tax:     ", federalTax)
    print("FICA Tax:        ", FICA_tax)
    print("Regular Pay:     ", regularPay)
    print("Overtime Pay:    ", overtimePay)
    print("Gross Pay:       ", grossPay)
    print("Total Deduction: ", totalDeduction)
    print("Net Pay:         ", netPay)
    print("\n")
#End of printAll


#10.    Declare and initialize variables
name = "Yasmeen Hart"
company = "Valdosta State University"
hours = 40
hourlyRate = 10.0
stateRate = 0.06
federalRate = 0.15
FICA_rate = 0.085

#11.    Invoke computePay function
regularPay, overtimePay, grossPay = computePay (hours,hourlyRate)

#12.    Invoke computeTaxes function
stateTax, federalTax, FICA_tax, totalDeduction, netPay = \
    computeTaxes (grossPay, stateRate, federalRate, FICA_rate)

#13.    Invoke printAll function
printAll (name, company, hours, hourlyRate,stateRate, \
              federalRate, FICA_rate, stateTax, federalTax,\
              FICA_tax, regularPay,overtimePay, grossPay,\
              totalDeduction, netPay)

#14.    Assign another set of hours and hourly rate
hours = 50
hourlyRate = 20.0

#15.    Invoke computePay function
regularPay, overtimePay, grossPay = computePay (hours,hourlyRate)

#16.    Invoke computeTaxes function
stateTax, federalTax, FICA_tax, totalDeduction, netPay = \
    computeTaxes (grossPay, stateRate, federalRate, FICA_rate)

#17.    Invoke printAll function
printAll (name, company, hours, hourlyRate,stateRate, \
              federalRate, FICA_rate, stateTax, federalTax,\
              FICA_tax, regularPay,overtimePay, grossPay,\
              totalDeduction, netPay)


