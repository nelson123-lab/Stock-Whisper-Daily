class StockPortfolio:
    def __init__(self):
        self.shares = []
        self.min_stock = float('inf')
        self.max_stock = 0
        self.total_cost = 0
        self.total_shares = 0
        self.profit_loss = 0
        self.average_cost = 0

    def add_stock(self, shares, price):
        self.shares.append((shares, price))
        self.total_cost += shares * price
        self.total_shares += shares
        self.min_stock = min(self.min_stock, price)
        self.max_stock = max(self.max_stock, price)
        if self.total_shares == 0:
            self.average_cost = 0
        self.average_cost = self.total_cost / self.total_shares

    def shares_needed_to_average_down(self, current_price, target_average):
        if current_price >= target_average:
            return 0
        needed_shares = (self.total_cost - target_average * self.total_shares) / (target_average - current_price)
        return max(0, needed_shares)

    def sell_stock(self, selling_price, no_of_stocks):
        if no_of_stocks > self.total_shares:
            raise ValueError("Cannot sell more shares than you own.")
        
        self.shares.append((no_of_stocks, selling_price))
        # Calculate profit or loss for the sold shares
        profit_loss_for_sale = abs(no_of_stocks) * (selling_price - self.average_cost)
        
        # Update portfolio's total shares and total cost
        self.total_shares += no_of_stocks # when selling number of shares will be already with a negative value.
        self.total_cost += no_of_stocks * self.average_cost
        
        # Update the portfolio's cumulative profit/loss
        self.profit_loss += profit_loss_for_sale
        


    def investment(self, investment, current_price):
        # Calculate the number of shares purchased with the investment
        new_shares = investment / current_price
        # Calculate the new total cost
        new_total_cost = self.total_cost + investment
        # Calculate the new total number of shares
        new_total_shares = self.total_shares + new_shares
        # Calculate the new average cost
        new_average_cost = new_total_cost / new_total_shares
        return new_shares, new_average_cost
    
    # def calculate_break_even(self, transactions):
    #     total_cost = 0
    #     total_sales = 0
    #     net_quantity = 0

    #     for quantity, price in transactions:
    #         if quantity > 0:
    #             total_cost += quantity * price
    #         else:
    #             total_sales += abs(quantity) * price
    #         net_quantity += quantity

    #     if net_quantity == 0:
    #         return None  # Avoid division by zero, no net position
    #     else:
    #         break_even_price = (total_cost - total_sales) / net_quantity
    #         return break_even_price
        
    def calculate_break_even(self):
        if self.total_shares == 0:
            break_even_price = 0
            return break_even_price
        else:
            break_even_price = (self.total_cost - self.profit_loss) / self.total_shares
            return break_even_price

def main():
    portfolio = StockPortfolio()
    current_price = float(input("Enter the current stock price: "))
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
        if shares < 0:
            portfolio.sell_stock(price, shares)
        else:
            portfolio.add_stock(shares, price)
    
    print(f"Average stock: ${portfolio.average_cost:.2f}")
    print(f"Capital: ${portfolio.total_cost:.2f}")
    print(f"Total number of shares: {portfolio.total_shares:.2f}")
    print(f"Market Value: {portfolio.total_shares * current_price:.2f}")
    print(f"Total return: {((portfolio.total_shares * current_price)-portfolio.total_cost):.2f}")
    print(f"Profit/Loss: {portfolio.profit_loss:.2f}")
    print(f"Shares: {portfolio.shares}")
    print(f"Minimum stock buy price: ${portfolio.min_stock:.2f}")
    print(f"Maximum stock buy price: ${portfolio.max_stock:.2f}")
    print(f"Break Even point: ${portfolio.calculate_break_even():.2f}")

    answer = input("How are you planning to average down ? (investment/ shares):")
    if answer.lower() == "shares":
        while True:
            target_average = float(input("Enter the target average price: "))
            needed_shares = portfolio.shares_needed_to_average_down(current_price, target_average)
            if needed_shares > 0:
                print(f"You need to buy at least {needed_shares:.2f} shares at ${current_price:.2f} to bring the average price below ${target_average:.2f} and this will cost ${(needed_shares*current_price):.2f}")
            else:
                print(f"Buying more shares at ${current_price:.2f} will not lower the average price to below ${target_average:.2f}")
            
            another_check = input("Do you want to check with another current price and target average? (yes/no): ")
            if another_check.lower() != 'yes':
                break
    elif answer.lower() == 'investment':
        while True:
            print("To check for the investment amount")
            investment = float(input("Enter the amount of money that you are planning to invest: "))
            new_shares, new_average_cost = portfolio.investment(investment, current_price)

            print(f"You can buy {new_shares:.2f} shares at ${current_price:.2f} to bring the average price to ${new_average_cost:.2f}")
            
            another_check = input("Do you want to check with another current price and target average? (yes/no): ")
            if another_check.lower() != 'yes':
                break
    else:
        pass

if __name__ == "__main__":
    main()

"""
Examples

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
1 @ 97.58
-2 @ 105.65
-2 @ 109.94
-8 @ 115.65
1 @ 114.97
-1 @ 118.5

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