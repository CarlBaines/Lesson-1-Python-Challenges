

def calculateProfit(dict):
    calculateProfit = round((dict['sell_price'] - dict['cost_price']) * dict['inventory'],0)
    print(calculateProfit)


#dictionary
calculateProfit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
})