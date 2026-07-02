# Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# -------------------------------
# Title
# -------------------------------
st.title("Expense Dashboard")
st.caption("Add your expenses to calculate and visualize your spending.")

# -------------------------------
# User Input
# -------------------------------

income = st.number_input(
    "Enter Monthly Income",
    min_value=0,
    step=100
)

amount = st.number_input(
    "Enter Expense Amount",
    min_value=0,
    step=10
)

category = st.selectbox(
    "Select Category",
    ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]
)

today = st.date_input(
    "Select Date",
    date.today()
)

button = st.button("Add Expense")

# -------------------------------
# Save Expense
# -------------------------------

if button:

    if amount == 0:
        st.error("Please enter an expense amount.")

    else:

        new_data = {
            "Date": [today],
            "Category": [category],
            "Amount": [amount]
        }

        new_expense = pd.DataFrame(new_data)

        old_data = pd.read_csv("expenses.csv")

        all_data = pd.concat(
            [old_data, new_expense],
            ignore_index=True
        )

        all_data.to_csv(
            "expenses.csv",
            index=False
        )

        st.success("Expense Added Successfully!")
        st.rerun()

# -------------------------------
# Read Expense Data
# -------------------------------

data = pd.read_csv("expenses.csv")

# -------------------------------
# Show Expense Records
# -------------------------------

st.header(" Expense Records")

st.dataframe(data)

# -------------------------------
# Delete Expense
# -------------------------------

st.header("🗑 Delete Expense")

if len(data) > 0:

    expense_list = []

    for i in range(len(data)):

        text = str(data.loc[i, "Date"]) + " | " + data.loc[i, "Category"] + " | ₹" + str(data.loc[i, "Amount"])

        expense_list.append(text)

    selected = st.selectbox(
        "Select Expense",
        expense_list
    )

    delete = st.button("Delete Expense")

    if delete:

        index = expense_list.index(selected)

        data = data.drop(index)

        data = data.reset_index(drop=True)

        data.to_csv("expenses.csv", index=False)

        st.success("Expense Deleted Successfully!")

        st.rerun()

# -------------------------------
# Charts
# -------------------------------

st.header(" Expense Analytics")

if len(data) > 0:

    # Pie Chart

    st.subheader(" Category Wise Expenses")

    category_data = data.groupby("Category")["Amount"].sum().reset_index()

    pie = px.pie(
        category_data,
        names="Category",
        values="Amount"
    )

    st.plotly_chart(pie)

    # Bar Chart

    st.subheader(" Category Spending")

    bar = px.bar(
        category_data,
        x="Category",
        y="Amount",
        color="Category"
    )

    st.plotly_chart(bar)

    # Line Chart

    st.subheader(" Expense Trend")

    line = px.line(
        data,
        x="Date",
        y="Amount",
        markers=True
    )

    st.plotly_chart(line)

# -------------------------------
# Expense Summary
# -------------------------------

if len(data) > 0:

    st.header(" Expense Summary")

    total_expense = data["Amount"].sum()

    balance = income - total_expense

    highest = category_data.loc[
        category_data["Amount"].idxmax(),
        "Category"
    ]

    st.write(" Total Expenses : ₹", total_expense)

    st.write(" Remaining Balance : ₹", balance)

    st.write(" Highest Spending Category :", highest)

# -------------------------------
# Rule-Based AI Suggestions
# -------------------------------

    st.header(" Smart AI Suggestions")

    food = 0
    shopping = 0
    travel = 0
    bills = 0

    for i in range(len(data)):

        if data.loc[i, "Category"] == "Food":
            food = food + data.loc[i, "Amount"]

        if data.loc[i, "Category"] == "Shopping":
            shopping = shopping + data.loc[i, "Amount"]

        if data.loc[i, "Category"] == "Travel":
            travel = travel + data.loc[i, "Amount"]

        if data.loc[i, "Category"] == "Bills":
            bills = bills + data.loc[i, "Amount"]

    if income > 0:

        if total_expense > income:

            st.error("Warning! You have exceeded your monthly income.")

        else:

            st.success("Your expenses are within your monthly income.")
   
    if total_expense > 0:

        if food > total_expense * 0.40:
            st.warning(" You spend more than 40% on Food.")

        if shopping > total_expense * 0.30:
            st.warning(" Shopping expenses are high.")

        if travel > total_expense * 0.20:
            st.info(" Travel expenses are increasing.")

        if bills > total_expense * 0.50:
            st.warning(" Bills take up a large share of your income.")

        if balance > income * 0.30:
            st.success(" Great! You are saving a healthy amount every month.")

# -------------------------------
# Reset Dashboard
# -------------------------------

st.subheader(" New Calculation")

reset = st.button("Clear All Expenses")

if reset:

    empty = pd.DataFrame(
        columns=["Date", "Category", "Amount"]
    )

    empty.to_csv(
        "expenses.csv",
        index=False
    )

    st.success("Dashboard Reset Successfully!")

    st.rerun()