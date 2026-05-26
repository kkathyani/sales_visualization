import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Dashboard")
st.markdown("Interactive Retail Sales Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("retail_sales_dataset.csv")

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    return df

df = load_data()

# ---------------- Sidebar ----------------

st.sidebar.header("Filter Data")

selected_category = st.sidebar.multiselect(
    "Select Product Category",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Filter data
filtered_df = df[
    (df["Product Category"].isin(selected_category))
    &
    (df["Gender"].isin(selected_gender))
]

# ---------------- KPI Cards ----------------

total_sales = filtered_df["Total Amount"].sum()
total_orders = filtered_df["Transaction ID"].count()
avg_sales = filtered_df["Total Amount"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${total_sales:,.0f}")

with col2:
    st.metric("Total Orders", total_orders)

with col3:
    st.metric("Average Sale", f"${avg_sales:,.2f}")

st.divider()

# ---------------- Monthly Sales Trend ----------------

filtered_df["Month"] = filtered_df["Date"].dt.strftime("%b")

month_order = [
    'Jan','Feb','Mar','Apr','May','Jun',
    'Jul','Aug','Sep','Oct','Nov','Dec'
]

monthly_sales = (
    filtered_df.groupby("Month")["Total Amount"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

fig1 = px.line(
    monthly_sales,
    x="Month",
    y="Total Amount",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- Category Revenue ----------------

category_sales = (
    filtered_df.groupby("Product Category")
    ["Total Amount"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    category_sales,
    x="Product Category",
    y="Total Amount",
    title="Revenue by Product Category"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Gender Distribution ----------------

gender_sales = (
    filtered_df.groupby("Gender")
    ["Total Amount"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    gender_sales,
    names="Gender",
    values="Total Amount",
    title="Gender-wise Spending"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- Age Distribution ----------------

fig4 = px.histogram(
    filtered_df,
    x="Age",
    title="Customer Age Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------- Dataset Preview ----------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df)