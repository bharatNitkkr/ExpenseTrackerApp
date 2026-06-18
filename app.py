from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash
)
from database import get_connection


app = Flask(__name__)

app.secret_key = "mysecretkey"  # for flash messages(pop up on screen)

#expenses = []  # Used for temporary memory in python as python list


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_expense():

    if request.method == 'POST':

        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO expenses (amount, category, description)
            VALUES (?, ?, ?)
        """, (amount, category, description))

        conn.commit()
        conn.close()
        
        flash("Expense added successfully!", "success")

        return redirect('/view')

    return render_template('add_expense.html')


@app.route('/view')
def view_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    # Total amount
    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses
    """)
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    # Number of entries
    cursor.execute("""
    SELECT COUNT(*)
    FROM expenses
    """)
    count = cursor.fetchone()[0]
    
    if count is None:
        count = 0
        
        
    cursor.execute("""
    SELECT MAX(amount)
    FROM expenses
    """)

    highest = cursor.fetchone()[0]

    if highest is None:
        highest = 0
      
        
    cursor.execute("""
    SELECT AVG(amount)
    FROM expenses
    """)

    average = cursor.fetchone()[0]
    average = round(average, 2)

    if average is None:
        average = 0
        
    cursor.execute("""
    SELECT category,
    SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    category_totals = cursor.fetchall()
        
    conn.close()
    
    

    return render_template(
        "view_expenses.html",
        expenses=expenses,
        total=total,
        count=count,
        highest=highest,
        average=average,
        category_totals=category_totals
    )  


@app.route('/delete/<int:id>')
def delete_expense(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()
    
    flash("Expense deleted successfully!", "danger")

    return redirect('/view')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':

        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']

        cursor.execute("""
            UPDATE expenses
            SET amount = ?, category = ?, description = ?
            WHERE id = ?
        """, (amount, category, description, id))

        conn.commit()
        conn.close()
        
        flash("Expense updated successfully!", "warning")

        return redirect('/view')

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (id,)
    )

    expense = cursor.fetchone()

    conn.close()

    return render_template(
        'edit_expense.html',
        expense=expense
    )


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True) 