from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Debt {self.id}: {self.amount} - {self.description} due on {self.due_date}>'