# 📊 Stock Market Dashboard – Stolker

A real-time stock market dashboard built with **Flask**, **yFinance**, and **Matplotlib** that displays key financial data and visual insights for publicly traded companies.

🔗 **[Live Demo](https://stolker.onrender.com/)**

---

## 🚀 Features

- 🔎 **Company Overview**: Fetch real-time data such as market cap, P/E ratio, revenue, and cash flow using the `yfinance` API.
- 📊 **Interactive Visualizations**: Auto-generated bar charts for quarterly financials and stock price trends using `Matplotlib`.
- 🧠 **OOP Design**: Modular, maintainable code using an object-oriented architecture (`StockVisualizer` class).
- 🎨 **Clean UI**: Responsive design using **HTML**, **Jinja2 Templates**, and **Custom CSS**.
- 📁 **Static Chart Rendering**: Efficient file handling for generating and displaying stock visuals.

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Data Source**: yFinance API
- **Visualization**: Matplotlib, Pandas
- **Frontend**: HTML, CSS, Jinja2
- **Deployment**: Render

---

## 🧪 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/vihansr/Stock-market-dashboard.git
cd Stock-market-dashboard

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
