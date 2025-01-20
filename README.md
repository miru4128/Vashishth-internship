# Student Attendance Tracker

## Project Overview
The Student Attendance Tracker is a web application designed for professors to manage student attendance efficiently. The application allows professors to log in, mark attendance for students in different divisions, and manage student records.

## Technology Stack
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite
- **Dependencies**: Flask, SQLite libraries

## Project Structure
```
student-attendance-tracker

├── app.py
├── templates
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── division.html
│   ├── add_student.html
│   └── remove_student.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
└── models.py
├── database
│   └── attendance.db
├── requirements.txt
└── README.md
```

## Setup Instructions
1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd student-attendance-tracker
   ```

2. **Install Dependencies**: 
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**: 
   Start the Flask application by executing:
   ```
   python app.py
   ```

4. **Access the Application**: 
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Features
- **Login System**: Professors can log in to access the application.
- **Attendance Management**: Professors can mark students as present or absent for specific days.
- **Student Management**: Add or remove students from the database.
- **Attendance Reports**: View attendance records for each student per month.

## Screenshots
(Include screenshots of the application here)

## Video Demonstration
(Include a link to a video demonstration of the application here)

## License
This project is licensed under the MIT License - see the LICENSE file for details.