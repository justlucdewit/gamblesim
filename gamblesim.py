from math import floor
from random import random

def mean(arr):
    sum = 0
    for i in arr:
        sum += i
    meanval = sum/len(arr)
    return meanval
    

class Gambler:
    def __init__(self, starting_money, starting_bid):
        self.money = starting_money
        self.bidamount = starting_bid

    def gamble(self):
        if self.money > 0:
            self.money -= self.bidamount
            number = floor(random()*100)+1
            if number == 100:#stonks
                self.money += self.bidamount*3
                return 2
            elif number >= 50:
                self.money += self.bidamount*2
                return 1
            else:
                return 0

def SET(n, numberofbidders, numberofbids, startingamount):
    #simulate
    market = []

    for i in range(numberofbidders):
        luke = Gambler(startingamount, n)
        balances = []
        for i in range(numberofbids):
            luke.gamble()
            balances.append(luke.money)
        market.append(balances)
    return market