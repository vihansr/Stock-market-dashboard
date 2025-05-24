from flask import Flask, render_template, request, url_for, redirect, flash
from Stock_details import StockDetails

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        symbol = request.form.get('stock_symbol', '').strip().upper()

        if not symbol:
            flash("Please enter a stock symbol.", "warning")
            return redirect(url_for('index'))

        return redirect(url_for('stock', stock_symbol=symbol))

    return render_template("index.html")


@app.route("/stocks/<stock_symbol>")
def stock(stock_symbol):
    s1 = StockDetails(stock_symbol)
    info = s1.stock_info()

    if not info:
        flash(f"No data found for stock symbol: {stock_symbol}", "danger")
        return redirect(url_for('index'))

    chart_file = s1.price_chart()
    cashflow_chart = s1.cashflow_chart()
    financials_chart = s1.financials_chart()
    balance_sheet_chart = s1.balance_sheet_chart()

    if not all([chart_file, cashflow_chart, financials_chart, balance_sheet_chart]):
        flash("Some charts could not be generated. Please try another stock.", "warning")

    return render_template(
        "stock.html",
        info=info,
        stock_symbol=stock_symbol,
        chart_file=chart_file,
        cashflow_chart=cashflow_chart,
        financials_chart=financials_chart,
        balance_sheet_chart=balance_sheet_chart
    )

if __name__ == "__main__":
    app.run(debug=True)
