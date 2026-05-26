# 📊 Retail Sales Dashboard

An interactive Retail Sales Dashboard built using Streamlit, Pandas, and Plotly for analyzing customer purchasing behavior and sales trends. This dashboard provides visual insights into retail transactions through interactive charts and filtering options.

## 🚀 Project Overview

This project uses a public retail sales dataset to analyze:

- Sales performance over time
- Product category revenue
- Customer demographics
- Purchase trends
- Gender-wise spending patterns

The dashboard allows users to filter and interact with data dynamically.

---

## 📁 Dataset Information

The dataset contains retail transaction records with the following attributes:

| Feature | Description |
|-----------|------------|
| Transaction ID | Unique transaction identifier |
| Date | Purchase date |
| Customer ID | Unique customer identifier |
| Gender | Customer gender |
| Age | Customer age |
| Product Category | Product category purchased |
| Quantity | Quantity purchased |
| Price per Unit | Product price per unit |
| Total Amount | Total purchase amount |

Dataset Size:

- Total Records: 1000
- Total Features: 9

---

## ✨ Dashboard Features

✔ KPI Cards
- Total Sales
- Total Orders
- Average Sale Value

✔ Interactive Filters
- Product Category filter
- Gender filter

✔ Visualizations
- Monthly Sales Trend
- Revenue by Product Category
- Gender-wise Spending Distribution
- Customer Age Distribution

✔ Dataset Preview Table

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- NumPy

---

## 📂 Project Structure

retail-sales-dashboard/
│
├── app.py
├── retail_sales_dataset.csv
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml

---

## ⚙ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to project folder:

```bash
cd retail-sales-dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Add sales forecasting
- Add customer segmentation analysis
- Add advanced filtering options
- Add downloadable reports
- Integrate live data sources

---

## 👤 Author

K Venkata Sai Kathyani
