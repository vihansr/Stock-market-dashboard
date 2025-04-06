import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

class StockDetails:
    def __init__(self, symbol):
        self.symbol= symbol
        self.stock = yf.Ticker(self.symbol)
        self.info = self.stock.info
        self.data = pd.DataFrame(self.stock.history(period="3mo"))

    def stock_info(self):
        return self.info

    def price_chart(self):
        plt.figure(figsize=(10, 4))

        # Determine color based on price change
        start_price = self.data['Close'].iloc[0]
        end_price = self.data['Close'].iloc[-1]
        color = 'green' if end_price >= start_price else 'red'

        # Plot with selected color
        plt.plot(self.data.index, self.data['Close'], color=color, linewidth=2)
        plt.title(f"{self.symbol} Price Chart")
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.grid(True)

        # Save chart image
        filename = f"{self.symbol}_price_chart_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        filepath = os.path.join("static", filename)

        plt.tight_layout()
        plt.savefig(filepath)
        plt.close()

        return filename

    def cashflow_chart(self):
        df = pd.DataFrame(self.stock.cashflow)
        df.loc['Sum'] = df.sum()
        net_cashflow = df.loc['Sum'] / 100000000  # Scale down for readability

        net_cashflow_data = {
            'Q1': net_cashflow[0],
            'Q2': net_cashflow[1],
            'Q3': net_cashflow[2],
            'Q4': net_cashflow[3]
        }

        # Determine colors based on positive or negative values
        colors = ['green' if val >= 0 else 'red' for val in net_cashflow_data.values()]

        plt.figure(figsize=(10, 6))
        plt.bar(net_cashflow_data.keys(), net_cashflow_data.values(), color=colors)

        plt.xlabel("Quarter")
        plt.ylabel("Cashflow (In 100 Millions)")
        plt.title("Quarterly Cashflow")
        plt.grid(axis='y')

        filename = f"{self.symbol}_cashflow_chart_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        filepath = os.path.join("static", filename)
        plt.tight_layout()
        plt.savefig(filepath)
        plt.close()

        return filename

    def financials_chart(self):
        df = pd.DataFrame(self.stock.financials)
        df.loc['Sum'] = df.sum()
        net_fin = df.loc['Sum'] / 100000000

        net_financials_data = {
            'Q1': net_fin[0],
            'Q2': net_fin[1],
            'Q3': net_fin[2],
            'Q4': net_fin[3]
        }

        plt.figure(figsize=(10, 6))
        plt.bar(net_financials_data.keys(), net_financials_data.values(), color='green')

        plt.xlabel("Quarter")
        plt.ylabel("Financials (In 100 Millions)")
        plt.title("Quarterly Financials")

        filename = f"{self.symbol}_financials_chart_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        filepath = os.path.join("static", filename)
        plt.savefig(filepath)


        return filename

    def balance_sheet_chart(self):
        df = pd.DataFrame(self.stock.balance_sheet)
        df.loc['Sum'] = df.sum()
        net_balance = df.loc['Sum'] / 100000000

        net_balance_data = {
            'Q1': net_balance[0],
            'Q2': net_balance[1],
            'Q3': net_balance[2],
            'Q4': net_balance[3]
        }

        plt.figure(figsize=(10, 6))
        plt.bar(net_balance_data.keys(), net_balance_data.values(), color='skyblue')

        plt.xlabel("Quarter")
        plt.ylabel("Balance Sheet (In 100 Millions)")
        plt.title("Quarterly Balance Sheet")

        filename = f"{self.symbol}_balance_sheet_chart_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        filepath = os.path.join("static", filename)
        plt.savefig(filepath)


        return filename

