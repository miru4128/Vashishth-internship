from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    division = db.Column(db.String(10), nullable=False)
    attendance_records = db.relationship('Attendance', backref='student', lazy=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # 'Present' or 'Absent'

def add_student(name, division):
    new_student = Student(name=name, division=division)
    db.session.add(new_student)
    db.session.commit()

def remove_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()

def mark_attendance(student_id, date, status):
    attendance_record = Attendance(student_id=student_id, date=date, status=status)
    db.session.add(attendance_record)
    db.session.commit()

def get_attendance_report(student_id, month, year):
    records = Attendance.query.filter(
        Attendance.student_id == student_id,
        db.extract('month', Attendance.date) == month,
        db.extract('year', Attendance.date) == year
    ).all()
    present_days = sum(1 for record in records if record.status == 'Present')
    absent_days = sum(1 for record in records if record.status == 'Absent')
    return present_days, absent_days