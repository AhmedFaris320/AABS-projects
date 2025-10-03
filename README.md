# 🎓 Student Performance App

A **Streamlit-based project** to analyze student marks, calculate GPA, assign grades, generate PDF reports, and visualize performance.  
This project is built with **Object-Oriented Programming (OOP)** and demonstrates **clean file structuring** in Python.

---

## 📂 Project Structure
│── app.py # Main Streamlit entry point
│── modules/
│ │── student.py # Student class (validation, GPA, grade assignment)
│ │── report.py # Report class (manages multiple students, creates DataFrame)
│ │── pdf_generator.py # Generates PDF reports using ReportLab
│ │── charts.py # Functions for visualizations
│── utils/
│ │── file_utils.py # CSV validation and helper functions
│── data/
│ └── sample_students.csv # Example dataset
│── requirements.txt # Python dependencies
│── README.md # Documentation

## ✨ Features

- 📌 Upload student data from CSV  
- 🔎 Validate student marks and input  
- 📊 Calculate GPA and assign grades (A, B, C, D)  
- 📑 Generate **summary reports**  
- 📈 Visualize data with **charts & heatmaps**  
- 📄 Export a **PDF report** with tables + charts  
- ⚡ Built with **modular structure & OOP concepts**  

---

## 🛠️ Technologies Used

- **Streamlit** → Web UI  
- **Pandas** → Data handling  
- **NumPy** → Calculations  
- **Matplotlib** & **Seaborn** → Charts  
- **ReportLab** → PDF generation  

📘 Module Overview
🔹 student.py

Defines the Student class:

Validates marks (0–100)

Calculates GPA (average marks / 25)

Assigns grades (A, B, C, D)

🔹 report.py

Handles multiple students:

Converts data into a Pandas DataFrame

Summarizes GPA & Grades

Exports professional reports:

Title & summary statistics

Student-level table

Charts embedded into the PDF

🔹 charts.py

Reusable chart functions:

Bar chart (average marks per subject)

Line chart (GPA trends)

Heatmap (correlations)

Count plot (grade distribution)

🔹 utils/file_utils.py

Helper functions:

Read & validate CSV file

Ensure required columns:
roll_no, name, math, science, english

Check for empty or invalid values
