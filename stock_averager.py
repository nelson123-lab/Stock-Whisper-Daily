class StockPortfolio:
    def __init__(self):
        self.shares = []
        self.stock_prices = []
        self.total_cost = 0
        self.total_shares = 0

    def add_stock(self, shares, price):
        self.shares.append((shares, price))
        self.stock_prices.append(price)
        self.total_cost += shares * price
        self.total_shares += shares

    def average_cost(self):
        if self.total_shares == 0:
            return 0
        return self.total_cost / self.total_shares

    def shares_needed_to_average_down(self, current_price, target_average):
        if current_price >= target_average:
            return 0
        needed_shares = (self.total_cost - target_average * self.total_shares) / (target_average - current_price)
        return max(0, needed_shares)

    def share_pricing_overview(self):
        lowest_price = min(self.stock_prices)
        return lowest_price


def main():
    portfolio = StockPortfolio()
    
    # Read stock purchases from file
    filename = "stock_input.txt"
    with open(filename, 'r') as file:
        data = file.read()
    
    # Split the input data into individual purchases
    purchases = data.split("\n")
    for purchase in purchases:
        shares, price = purchase.split(" @ ")
        shares = float(shares)
        price = float(price)
        portfolio.add_stock(shares, price)
    
    print(f"Average cost of your stock: ${portfolio.average_cost():.2f}")
    print(f"The lowest price of your stock: ${portfolio.share_pricing_overview():.2f}")
    
    while True:
        current_price = float(input("Enter the current stock price: "))
        target_average = float(input("Enter the target average price: "))
        needed_shares = portfolio.shares_needed_to_average_down(current_price, target_average)
        if needed_shares > 0:
            print(f"You need to buy at least {needed_shares:.2f} shares at ${current_price:.2f} to bring the average price below ${target_average:.2f} and this will cost ${(needed_shares*current_price):.2f}")
        else:
            print(f"Buying more shares at ${current_price:.2f} will not lower the average price to below ${target_average:.2f}")
        
        another_check = input("Do you want to check with another current price and target average? (yes/no): ")
        if another_check.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

"""
NVDIA
1 @ 128.59
1 @ 126.46
0.2 @ 125.75
0.6 @ 126
0.7 @ 118.71
1 @ 116.85
1 @ 112.12
1 @ 107.81
0.9 @ 112.04
1 @ 104.88
1 @ 100.96
1 @ 101.02
0.6 @ 99.67

Micron Technology
1 @ 134.79
1 @ 132.58
0.7 @ 130.89
0.9 @ 130.97
0.4 @ 128.62
1 @ 127.95
1 @ 114.64
1 @ 115.69
0.7 @ 115.91
1 @ 106.91
1 @ 105.92
1 @ 107.78
1 @ 104.36
1 @ 90.72
1 @ 90.20
0.3 @ 88.90
"""