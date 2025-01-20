// src/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to validate login form
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (!username || !password) {
                event.preventDefault();
                alert('Please fill in both fields.');
            }
        });
    }

    // Function to handle attendance marking
    const attendanceForm = document.getElementById('attendanceForm');
    if (attendanceForm) {
        attendanceForm.addEventListener('submit', function(event) {
            const presentStudents = document.querySelectorAll('input[name="attendance"]:checked');
            if (presentStudents.length === 0) {
                event.preventDefault();
                alert('Please mark at least one student as present or absent.');
            }
        });
    }

    // Function to dynamically update student list on add/remove
    const studentList = document.getElementById('studentList');
    const addStudentForm = document.getElementById('addStudentForm');
    if (addStudentForm) {
        addStudentForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const studentName = document.getElementById('studentName').value;
            if (studentName) {
                const newStudent = document.createElement('li');
                newStudent.textContent = studentName;
                studentList.appendChild(newStudent);
                document.getElementById('studentName').value = ''; // Clear input
            } else {
                alert('Please enter a student name.');
            }
        });
    }
});
