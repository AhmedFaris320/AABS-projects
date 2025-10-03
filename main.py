# Import required libraries for the Streamlit web application
import streamlit as st  # For building the interactive web interface
import pandas as pd     # For data manipulation and analysis
import tempfile, os     # For temporary file handling and path operations
from io import StringIO # For in-memory string operations (CSV downloads)

# Import custom modules from the project package
from project.modules.report import StudentReport           # For processing student data
from project.modules.pdfgenerator import PDFReportGenerator # For generating PDF reports
from project.modules import charts                         # For creating data visualizations
from project.utils.file_utils import read_and_validate_csv # For CSV file validation


# Configure the Streamlit page settings and create the main UI
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📊 Student Performance Analysis System")
st.write("Upload a CSV file of student marks and explore insights!")

# Create a file uploader widget for CSV files
uploaded_file = st.file_uploader("Upload students.csv", type=["csv"])


# Main application logic - execute only when a file is uploaded
if uploaded_file:
	# Step 1: Read and validate the uploaded CSV file
	df = read_and_validate_csv(uploaded_file)
	
	# Step 2: Process the raw data through the StudentReport class
	# This validates marks, calculates GPAs, and assigns grades
	report = StudentReport(df)
	df = report.to_dataframe()  # Get enhanced DataFrame with GPA and grades

	# Step 3: Display the processed student data in a table
	st.subheader("📌 Student Data")
	st.dataframe(df)  # Interactive table showing all student information

	# Step 4: Provide CSV download functionality for the analyzed data
	csv_buffer = StringIO()  # Create in-memory string buffer
	df.to_csv(csv_buffer, index=False)  # Convert DataFrame to CSV format
	st.download_button("📥 Download Analyzed Data (CSV)", csv_buffer.getvalue(),
					  file_name="analyzed_students.csv", mime="text/csv")

	# Step 5: Generate and display summary statistics
	st.subheader("📊 Summary Statistics")
	summary = df.describe()  # Calculate statistical summary (mean, std, min, max, etc.)
	st.write(summary)        # Display the summary table

	# Step 6: Create visualizations and generate PDF report
	st.subheader("📈 Visualizations")
	chart_files = []  # List to store file paths of generated charts
	
	# Use temporary directory to store chart images (automatically cleaned up)
	with tempfile.TemporaryDirectory() as tmp_dir:
		# Define file paths for each chart type
		avg_file = os.path.join(tmp_dir, "avg.png")        # Average marks per subject
		gpa_file = os.path.join(tmp_dir, "gpa.png")        # GPA trend by roll number
		heatmap_file = os.path.join(tmp_dir, "heatmap.png") # Correlation heatmap
		grade_file = os.path.join(tmp_dir, "grade.png")     # Grade distribution

		# Generate all charts and add their file paths to the list
		charts.save_avg_subject_chart(df, avg_file); chart_files.append(avg_file)
		charts.save_gpa_trend_chart(df, gpa_file); chart_files.append(gpa_file)
		charts.save_heatmap(df, heatmap_file); chart_files.append(heatmap_file)
		charts.save_grade_distribution(df, grade_file); chart_files.append(grade_file)

		# Step 7: Generate comprehensive PDF report
		pdf_gen = PDFReportGenerator(df, summary, chart_files)
		pdf_buffer = pdf_gen.generate()  # Create PDF in memory
		
		# Provide PDF download button
		st.download_button("📑 Download PDF Report", pdf_buffer,
						  file_name="student_report.pdf", mime="application/pdf")
		# Note: Temporary files are automatically deleted when exiting this block
else:
	# Display instructions when no file is uploaded
	st.info("👆 Upload a CSV file to get started.")