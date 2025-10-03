<h1 align="center">🎓 Student Performance App</h1>

<p align="center">
A <b>Streamlit-based project</b> to analyze student marks, calculate GPA, assign grades, generate PDF reports, and visualize performance.<br>
This project is built with <b>Object-Oriented Programming (OOP)</b> and demonstrates <b>clean file structuring</b> in Python.
</p>

---

<h2>📂 Project Structure</h2>

<pre>
│── app.py                  # Main Streamlit entry point
│── modules/
│   │── student.py          # Student class (validation, GPA, grade assignment)
│   │── report.py           # Report class (manages multiple students, creates DataFrame)
│   │── pdf_generator.py    # Generates PDF reports using ReportLab
│   │── charts.py           # Functions for visualizations
│── utils/
│   │── file_utils.py       # CSV validation and helper functions
│── data/
│   └── sample_students.csv # Example dataset
│── requirements.txt        # Python dependencies
│── README.md               # Documentation
</pre>

---

<h2>✨ Features</h2>

<ul>
<li>📌 Upload student data from CSV</li>
<li>🔎 Validate student marks and input</li>
<li>📊 Calculate GPA and assign grades (A, B, C, D)</li>
<li>📑 Generate <b>summary reports</b></li>
<li>📈 Visualize data with <b>charts & heatmaps</b></li>
<li>📄 Export a <b>PDF report</b> with tables + charts</li>
<li>⚡ Built with <b>modular structure & OOP concepts</b></li>
</ul>

---

<h2>🛠️ Technologies Used</h2>

<ul>
<li><b>Streamlit</b> → Web UI</li>
<li><b>Pandas</b> → Data handling</li>
<li><b>NumPy</b> → Calculations</li>
<li><b>Matplotlib</b> & <b>Seaborn</b> → Charts</li>
<li><b>ReportLab</b> → PDF generation</li>
</ul>

---

<h2>📘 Module Overview</h2>

<details>
<summary>🔹 <b>student.py</b></summary>
<ul>
<li>Validates marks (0–100)</li>
<li>Calculates GPA (average marks / 25)</li>
<li>Assigns grades (A, B, C, D)</li>
</ul>
</details>

<details>
<summary>🔹 <b>report.py</b></summary>
<ul>
<li>Handles multiple students</li>
<li>Converts data into a <b>Pandas DataFrame</b></li>
<li>Summarizes GPA & Grades</li>
</ul>
</details>

<details>
<summary>🔹 <b>pdf_generator.py</b></summary>
<ul>
<li>Exports professional reports:</li>
<li>Title & summary statistics</li>
<li>Student-level table</li>
<li>Charts embedded into the PDF</li>
</ul>
</details>

<details>
<summary>🔹 <b>charts.py</b></summary>
<ul>
<li>Bar chart (average marks per subject)</li>
<li>Line chart (GPA trends)</li>
<li>Heatmap (correlations)</li>
<li>Count plot (grade distribution)</li>
</ul>
</details>

<details>
<summary>🔹 <b>utils/file_utils.py</b></summary>
<ul>
<li>Read & validate CSV file</li>
<li>Ensure required columns:
<code>roll_no, name, math, science, english</code></li>
<li>Check for empty or invalid values</li>
</ul>
</details>

---

<h2>📂 Example Dataset</h2>

<pre>
roll_no,name,math,science,english
1,Ali,85,90,78
2,Sara,92,88,95
3,Ahmed,70,65,80
</pre>

---

<h2>📊 Visualizations</h2>

<ul>
<li>📊 Average Marks per Subject</li>
<li>📈 GPA Trend by Roll No</li>
<li>🔥 Correlation Heatmap</li>
<li>🏆 Grade Distribution</li>
</ul>

---

<h2>📦 requirements.txt</h2>

<pre>
streamlit
pandas
numpy
matplotlib
seaborn
reportlab
</pre>

---

<h2>🤝 Contributing</h2>
<p>1. Fork the repo<br>
2. Create a new branch (<code>feature-new-chart</code>)<br>
3. Commit your changes<br>
4. Push & open a Pull Request 🚀</p>

---

<h2>📄 License</h2>
<p>Licensed under the <b>MIT License</b>.<br>
You are free to use and modify.</p>

---

<h2>👨‍💻 Author</h2>

<p><b>Ahmed Faris</b><br>
🌐 GitHub: <a href="https://github.com/AhmedFaris320">AhmedFaris320</a></p>
