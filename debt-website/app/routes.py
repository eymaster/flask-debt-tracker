from flask import render_template, request, redirect, url_for
from .models import Debt
from . import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debts', methods=['GET', 'POST'])
def debts():
    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        due_date = request.form['due_date']
        new_debt = Debt(amount=amount, description=description, due_date=due_date)
        db.session.add(new_debt)
        db.session.commit()
        return redirect(url_for('debts'))
    
    all_debts = Debt.query.all()
    return render_template('debts.html', debts=all_debts)