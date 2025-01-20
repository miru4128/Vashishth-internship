from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Student, Attendance
import os

app = Flask(__name__)
app.secret_key = '639-146-633'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users/mihirraut/Vaisiti_intership/final/student-attendance-tracker/database/attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implement login logic here
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/division', methods=['GET', 'POST'])
def division():
    if request.method == 'POST':
        # Implement attendance marking logic here
        return redirect(url_for('dashboard'))
    return render_template('division.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Implement student addition logic here
        return redirect(url_for('dashboard'))
    return render_template('add_student.html')

@app.route('/remove_student', methods=['GET', 'POST'])
def remove_student():
    if request.method == 'POST':
        # Implement student removal logic here
        return redirect(url_for('dashboard'))
    return render_template('remove_student.html')

if __name__ == '__main__':
    app.run(debug=True)