#***********************************************************
#	Purpose:	Getting started with Python. Creating and running 
#			Python.
#			
#	Input:		Stock name, price, purchase and sale dates, commission rate
#	Output:		Net amount, total price, total paid
#	Author:		<Yasmeen Hart>
#	Date:		<Sept 3, 2020>
#	Class:		<CS 1010>
#	Program:	#3 (MyInvestment3.py)
#***********************************************************

#allows the user to input information about their stock
def getStockInformation():
    stockName = str(input("Enter the name of the stock: "))
    shares = int(input("Enter the number of shares: "))
    commissionRate = float(input("Enter commission rate: "))
    commissionRate *= 100
    return stockName, shares, commissionRate

#gets information from the user about the transaction
def transaction():
    purchaseDate = str(input("Enter the date of the transaction: "))
    sharePrice = float(input("Enter the share price: "))
    return purchaseDate, sharePrice

#computes data about the stock
def computeTransactionCommissionAndCost(shares, sharePrice, commissionRate):
    totalPrice = shares * sharePrice
    commission = commissionRate * totalPrice
    totalPaid = totalPrice + commissionRate
    return totalPrice, commission, totalPaid

#returns all information about the stock 
def printAll (stockName, shares, commissionRate, purchaseDate, purchaseSharePrice,saleDate,
              saleSharePrice, purchaseSharesCost, purchaseCommission, purchaseTotalCost,
              saleSharesCost, saleCommission, saleTotalCost, totalCommission, netAmount):
    print("Stock name:              ", stockName)
    print("Number of shares:        ", shares)
    print("Commission rate:         ", commissionRate, "%")
    print("\n")
    
    print("Purchase date:           ", purchaseDate)
    print("Purchase share price:    ", purchaseSharePrice)
    print("Purchase shares price:   ", purchaseSharePrice*shares)
    print("Purchase commission:     ", purchaseSharePrice*commissionRate)
    print("\n")
    
    print("Sale date:               ", saleDate)
    print("Sale share cost:         ", saleSharesCost)
    print("Sale shares cost:        ", saleSharesCost*shares)
    print("Sale commission:         ", saleCommission)
    print("Sale total cost:         ", saleTotalCost)
    print("\n")
    
    print("Total commission:        ", totalCommission)
    print("Net amount:              ", netAmount)

#calls all functions
stockName, shares, commissionRate = getStockInformation()

print ("\n\nEnter Stock Purchase Date and Purchase Share Price\n")
purchaseDate, purchaseSharePrice = transaction()

print ("\n\nEnter Stock Sale Date and Sale Share Price\n")
saleDate, saleSharePrice = transaction()

purchaseSharesCost, purchaseCommission, purchaseTotalCost = computeTransactionCommissionAndCost (shares, purchaseSharePrice, commissionRate)

saleSharesCost, saleCommission, saleTotalCost = computeTransactionCommissionAndCost (shares, saleSharePrice, commissionRate)

totalCommission = purchaseCommission + saleCommission

netAmount = saleTotalCost - purchaseTotalCost

printAll(stockName, shares, commissionRate, purchaseDate, purchaseSharePrice,
          saleDate,saleSharePrice, purchaseSharesCost, purchaseCommission, purchaseTotalCost,
          saleSharesCost, saleCommission, saleTotalCost, totalCommission, netAmount)

