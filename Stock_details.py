import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

class StockDetails:
    def __init__(self, symbol):
        self.symbol = symbol
        try:
            self.stock = yf.Ticker(self.symbol)
            self.info = self.stock.info or {}
            self.data = pd.DataFrame(self.stock.history(period="3mo"))
        except Exception as e:
            print(f"[ERROR] Initialization failed for symbol '{symbol}': {e}")
            self.stock = None
            self.info = {}
            self.data = pd.DataFrame()

    def stock_info(self):
        if not self.info:
            print(f"[WARNING] No info available for symbol '{self.symbol}'")
        return self.info

    def price_chart(self):
        try:
            if self.data.empty:
                raise ValueError("No price data available")

            plt.figure(figsize=(10, 4))
            start_price = self.data['Close'].iloc[0]
            end_price = self.data['Close'].iloc[-1]
            color = 'green' if end_price >= start_price else 'red'

            plt.plot(self.data.index, self.data['Close'], color=color, linewidth=2)
            plt.title(f"{self.symbol} Price Chart")
            plt.xlabel("Date")
            plt.ylabel("Closing Price")
            plt.grid(True)

            filename = f"{self.symbol}_price_chart_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            filepath = os.path.join("static", filename)

            plt.tight_layout()
            plt.savefig(filepath)
            plt.close()
            return filename

        except Exception as e:
            print(f"[ERROR] Failed to generate price chart for {self.symbol}: {e}")
            return None

    def cashflow_chart(self):
        try:
            df = pd.DataFrame(self.stock.cashflow)
            if df.empty:
                raise ValueError("Cashflow data unavailable")

            df.loc['Sum'] = df.sum()
            net_cashflow = df.loc['Sum'] / 100000000

            net_cashflow_data = {
                'Q1': net_cashflow[0],
                'Q2': net_cashflow[1],
                'Q3': net_cashflow[2],
                'Q4': net_cashflow[3]
            }

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

        except Exception as e:
            print(f"[ERROR] Failed to generate cashflow chart for {self.symbol}: {e}")
            return None

    def financials_chart(self):
        try:
            df = pd.DataFrame(self.stock.financials)
            if df.empty:
                raise ValueError("Financials data unavailable")

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
            plt.close()
            return filename

        except Exception as e:
            print(f"[ERROR] Failed to generate financials chart for {self.symbol}: {e}")
            return None

    def balance_sheet_chart(self):
        try:
            df = pd.DataFrame(self.stock.balance_sheet)
            if df.empty:
                raise ValueError("Balance sheet data unavailable")

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
            plt.close()
            return filename

        except Exception as e:
            print(f"[ERROR] Failed to generate balance sheet chart for {self.symbol}: {e}")
            return None
