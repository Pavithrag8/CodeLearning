'''Given a array of numbers representing the stock prices of a company in chronological order, write a 
function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars 
and sell it at 10 dollars.'''
stock_prices = [9, 11, 8, 20, 7, 10]
profit = 0
for i in range(0,len(stock_prices)):
    for j in range(i+1, len(stock_prices)):
        if profit < stock_prices[j] - stock_prices[i]:
            profit = stock_prices[j] - stock_prices[i]
            stock = stock_prices[i]
            selling_price = stock_prices[j]
print "If we  buy stock {} and sell it for {} we get profit {}".format(stock, selling_price, profit)


