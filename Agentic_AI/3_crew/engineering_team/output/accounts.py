class Account:
    def __init__(self, account_id: str, initial_deposit: float):
        self.account_id = account_id
        self.balance = initial_deposit
        self.initial_deposit = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({'type': 'withdraw', 'amount': amount})
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int, get_share_price) -> bool:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        price_per_share = get_share_price(symbol)
        total_price = price_per_share * quantity
        if self.balance >= total_price:
            self.balance -= total_price
            self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
            self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price_per_share})
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int, get_share_price) -> bool:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self.holdings.get(symbol, 0) >= quantity:
            price_per_share = get_share_price(symbol)
            total_price = price_per_share * quantity
            self.balance += total_price
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price_per_share})
            return True
        return False

    def calculate_portfolio_value(self, get_share_price) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self, get_share_price) -> float:
        return self.calculate_portfolio_value(get_share_price) - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings.copy()

    def get_transaction_history(self) -> list:
        return self.transactions.copy()

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)