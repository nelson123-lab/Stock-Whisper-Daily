class StockPortfolio:
    def __init__(self):
        self.shares = []
        self.total_cost = 0
        self.total_shares = 0
        self.profit_loss = 0
        self.average_cost = 0

    def add_stock(self, shares, price):
        self.total_cost += shares * price
        self.total_shares += shares
        self.average_cost = self.total_cost / self.total_shares

    def shares_needed_to_average_down(self, current_price, target_average):
        if current_price >= target_average:
            return 0
        needed_shares = (self.total_cost - target_average * self.total_shares) / (target_average - current_price)
        return max(0, needed_shares)

    def share_pricing_overview(self):
        if not self.shares:
            return None
        lowest_price = min(price for shares, price in self.shares)
        return lowest_price

    def sell_stock(self, selling_price, no_of_stocks):
        if no_of_stocks > self.total_shares:
            raise ValueError("Cannot sell more shares than you own.")
        
        # Calculate profit or loss for the sold shares
        profit_loss_for_sale = no_of_stocks * (selling_price - self.average_cost)
        
        # Update portfolio's total shares and total cost
        self.total_shares -= no_of_stocks
        self.total_cost -= no_of_stocks * self.average_cost
        
        # Update the portfolio's cumulative profit/loss
        self.profit_loss += profit_loss_for_sale
        
        # Remaining value of the portfolio at the current selling price
        remaining_value = self.total_shares * selling_price
        
        # Return the remaining number of shares, total profit/loss, remaining investment value, and profit/loss from this transaction
        return {
            "remaining_shares": self.total_shares,
            "total_profit_loss": self.profit_loss,
            "remaining_investment_value": remaining_value,
            "transaction_profit_loss": profit_loss_for_sale
        }

portfolio = StockPortfolio()
portfolio.add_stock(10, 100)  # Buy 10 shares at $100
portfolio.add_stock(10, 80)   # Buy 10 shares at $80
portfolio.sell_stock(85, 5)  # Sell 5 shares at $85
portfolio.sell_stock(80, 2)
portfolio.add_stock(11.7, 50)
portfolio.sell_stock(95, 15)
print(portfolio.average_cost)
print(portfolio.total_shares)
print(portfolio.profit_loss)