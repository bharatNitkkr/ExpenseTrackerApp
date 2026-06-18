# Expense Tracker App

A professional Expense Tracker web application built using Flask and SQLite.

## Features

- Add Expenses
- View Expenses
- Edit Expenses
- Delete Expenses
- Dashboard Statistics
    - Total Expenses
    - Total Entries
    - Highest Expense
    - Average Expense
- Category-wise Expense Analysis
- Flash Messages
- Responsive Bootstrap UI

---

## Tech Stack

- Python 3.13
- Flask
- HTML
- CSS
- Bootstrap 5
- SQLite
- Git & GitHub

---

## Folder Structure

ExpenseTrackerApp
│
├── app.py
├── database.py
├── init_db.py
├── static/
│ └── style.css
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── add_expense.html
│ ├── edit_expense.html
│ ├── view_expenses.html
│ └── about.html
└── README.md

---

## Installation

Clone the repository:

```bash
git clone https://github.com/bharatNitkkr/ExpenseTrackerApp.git
```

Go inside the folder:

```bash
cd ExpenseTrackerApp
```

Create virtual environment:

```bash
python -m venv myenv 
```

Activate it:

```bash
myenv\Scripts\activate
```

Install dependencies:

```bash
pip install flask
```

Run:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Charts and Analytics
- Monthly Reports
- User Authentication
- Dark Mode
- Export to Excel
- REST API
- Deployment

---

Built with using Flask.