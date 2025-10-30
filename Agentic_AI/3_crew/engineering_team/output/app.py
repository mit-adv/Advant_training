#```python
# app.py

import gradio as gr
from accounts import Account, get_share_price

# Initialize an account with default values
account = Account(account_id="user_001", initial_deposit=10000)

def create_account(initial_deposit):
    global account
    account = Account(account_id="user_001", initial_deposit=initial_deposit)
    return f"Account created with an initial deposit of ${initial_deposit}"

def deposit_funds(amount):
    try:
        account.deposit(amount)
        return f"Deposited ${amount}. Current balance: ${account.balance}"
    except ValueError as e:
        return str(e)

def withdraw_funds(amount):
    if account.withdraw(amount):
        return f"Withdrew ${amount}. Current balance: ${account.balance}"
    else:
        return "Insufficient funds for withdrawal."

def buy_shares(symbol, quantity):
    try:
        if account.buy_shares(symbol, quantity, get_share_price):
            return f"Bought {quantity} shares of {symbol}. Current balance: ${account.balance}"
        else:
            return "Insufficient funds to buy shares."
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        if account.sell_shares(symbol, quantity, get_share_price):
            return f"Sold {quantity} shares of {symbol}. Current balance: ${account.balance}"
        else:
            return "Insufficient shares to sell."
    except ValueError as e:
        return str(e)

def calculate_portfolio_value():
    value = account.calculate_portfolio_value(get_share_price)
    return f"Total portfolio value: ${value}"

def calculate_profit_loss():
    profit_loss = account.calculate_profit_loss(get_share_price)
    return f"Profit/Loss since initial deposit: ${profit_loss}"

def get_holdings():
    holdings = account.get_holdings()
    return f"Current holdings: {holdings}"

def get_transaction_history():
    transactions = account.get_transaction_history()
    return f"Transaction history: {transactions}"

interface = gr.Interface(
    fn=[
        create_account,
        deposit_funds,
        withdraw_funds,
        buy_shares,
        sell_shares,
        calculate_portfolio_value,
        calculate_profit_loss,
        get_holdings,
        get_transaction_history
    ],
    inputs=[
        gr.inputs.Number(label="Initial Deposit"),
        gr.inputs.Number(label="Amount to Deposit"),
        gr.inputs.Number(label="Amount to Withdraw"),
        gr.inputs.Textbox(label="Stock Symbol"),
        gr.inputs.Number(label="Quantity to Buy/Sell"),
        None,
        None,
        None,
        None
    ],
    outputs=[
        "text",
        "text",
        "text",
        "text",
        "text",
        "text",
        "text",
        "text",
        "text"
    ],
    live=False
)

if __name__ == "__main__":
    interface.launch()
#```