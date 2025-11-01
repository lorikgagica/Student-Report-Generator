# 🎓 Student Report Generator

A Python program that processes student grades from a CSV file, calculates averages, highlights the best student, and allows for easy searching by name.

---

## ✨ Features

- **Calculates average score** for each student across Math, Science, and English.
- **Highlights the best student** (highest average) in the report.
- **Search for any student by name** and see their scores, average, and status.
- **Calculates and displays the average for each subject** in the output report.
- **Generates a comprehensive CSV report with all data.**

---

## 🚀 How to Use

1. Prepare your `students.csv` file with columns: `Name`, `Math`, `Science`, `English`.
    ```
    Name,Math,Science,English
    Alice,89,95,91
    Bob,65,72,60
    Carol,99,88,93
    ```
2. Save your script as `generator.py`.
3. Open your terminal/command prompt and `cd` to the script’s folder.
4. Run: `python generator.py`
5. After processing, a new file `student_report.csv` is created in the folder.
6. You’ll be prompted to search for a student by name and see their info.

---

## 💡 Sample Output

- CSV report contains each student, their scores, average, status, and a column showing the best student.
- The last row displays the average for each subject:

Name,Math,Science,English,Average,Status,BestStudent
Alice,89,95,91,91.67,Pass,
Bob,65,72,60,65.67,Pass,
Carol,99,88,93,93.33,Pass,<<< BEST STUDENT
SUBJECT_AVERAGE,84.33,85,81.33,,,,

---

## 🔎 Example Student Search

Search for a student by name: Carol

Found: Carol, Math: 99, Science: 88, English: 93, Average: 93.33, Status: Pass
This student is the BEST student.

---

## 📄 License

MIT License — free to use, extend, and share.

---

Automate your grading reports and find your star student quickly!
