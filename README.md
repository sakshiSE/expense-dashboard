# Expense Dashboard

A simple expense dashboard built using Streamlit to help users manage and analyze personal expenses. The application allows users to add, delete, and clear expense records while providing interactive visualizations and basic rule-based spending insights.

## Live Demo

The application is deployed on Hugging Face Spaces:

https://huggingface.co/spaces/sakshiG0701/expense-dashboard

## Features

- Add new expense records
- Delete individual expense records
- Clear all expense records
- Calculate total expenses
- Visualize expenses through interactive charts
- Generate rule-based spending insights
- Simple and easy-to-use Streamlit interface

## Project Structure

```text
expense-dashboard/
│── app.py
│── expenses.csv
│── requirements.txt
```

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

## Installation

Clone the repository:

```bash
git clone https://github.com/sakshiSE/expense-dashboard.git
```

Navigate to the project directory:

```bash
cd expense-dashboard
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Data Storage

Expense records are stored in `expenses.csv`. Users can add, delete, or clear records through the application, and the dashboard updates automatically to reflect the latest data.
