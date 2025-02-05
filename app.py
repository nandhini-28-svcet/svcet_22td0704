from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Home route - Display all students
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Add a new student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        new_student = Student(name=name, email=email, phone=phone)
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_student.html')

# Edit a student's information
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.phone = request.form['phone']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)

# Delete a student
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)