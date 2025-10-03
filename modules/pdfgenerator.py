from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


class PDFReportGenerator:
    def __init__(self, df, summary, chart_files):
        """
        Initialize the PDFReportGenerator class.

        Args:
            df (DataFrame): Detailed student data (roll no, name, GPA, grade, etc.)
            summary (DataFrame): Summary statistics of student performance.
            chart_files (list): List of file paths to saved chart images.
        """
        self.df = df
        self.summary = summary
        self.chart_files = chart_files

    def generate(self):
        """
        Generate a PDF report containing:
        - Title
        - Summary statistics
        - Visualizations (charts)
        - Student-level detailed report

        Returns:
            BytesIO: A buffer containing the generated PDF.
        """
        # Create a memory buffer to store PDF output
        buffer = BytesIO()

        # Set up the PDF document with A4 page size
        doc = SimpleDocTemplate(buffer, pagesize=A4)

        # Get default styles for text formatting
        styles = getSampleStyleSheet()

        # Container for all PDF elements
        elements = []

        # --- Title ---
        elements.append(Paragraph("📊 Student Performance Report", styles['Title']))
        elements.append(Spacer(1, 12))  # Add spacing after title

        # --- Summary Statistics ---
        elements.append(Paragraph("Summary Statistics", styles['Heading2']))

        # Convert summary DataFrame to a ReportLab table
        summary_table = Table([self.summary.columns.to_list()] + self.summary.values.tolist())
        elements.append(summary_table)
        elements.append(Spacer(1, 12))

        # --- Visualizations ---
        elements.append(Paragraph("Visualizations", styles['Heading2']))

        # Loop through provided chart image files and insert into PDF
        for chart_file in self.chart_files:
            elements.append(Image(chart_file, width=400, height=250))
            elements.append(Spacer(1, 12))

        # --- Student-Level Report ---
        elements.append(Paragraph("Student-Level Report", styles['Heading2']))

        # Create table headers
        student_table_data = [["Roll No", "Name", "GPA", "Grade"]]

        # Loop through dataframe rows and add student details
        for _, row in self.df.iterrows():  # pyright: ignore[reportUndefinedVariable]
            student_table_data.append([row["roll_no"], row["name"], row["GPA"], row["Grade"]])

        # Create student detail table and align to left
        student_table = Table(student_table_data, hAlign="LEFT")
        elements.append(student_table)

        # Build the PDF with all elements
        doc.build(elements)

        # Reset buffer position to start
        buffer.seek(0)

        # Return PDF buffer
        return buffer
