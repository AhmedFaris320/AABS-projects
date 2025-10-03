# Import required libraries for data manipulation and student processing
import pandas as pd  # For DataFrame operations and data handling
from .student import Student  # Import the Student class from the same package


# Class to manage and process student reports
class StudentReport:
	# Initialize the report with a DataFrame containing raw student data
	def __init__(self, df):
		self.df = df  # Store the original DataFrame with student marks
		self.students = self.create_students()  # Create Student objects from DataFrame rows

	# Create Student objects from each row in the DataFrame
	def create_students(self):
		# Use list comprehension to iterate through DataFrame rows
		# For each row, create a Student object with roll_no, name, and subject marks
		# The Student class will automatically calculate GPA and assign grades
		return [
			Student(row["roll_no"], row["name"], row["math"], row["science"], row["english"])
			for _, row in self.df.iterrows()  # iterrows() returns (index, row) tuples
		]

	# Convert the list of Student objects back to a DataFrame with calculated values
	def to_dataframe(self):
		# Create a new DataFrame from Student objects with additional computed fields
		# Each Student object now has GPA and Grade calculated based on their marks
		return pd.DataFrame([{
			"roll_no": s.roll_no,        # Student's roll number
			"name": s.name,              # Student's name
			"math": s.math,              # Math marks (validated)
			"science": s.science,        # Science marks (validated)
			"english": s.english,        # English marks (validated)
			"GPA": s.gpa,               # Calculated GPA (0-4 scale)
			"Grade": s.grade            # Assigned letter grade (A, B, C, D)
		} for s in self.students])      # Iterate through all Student objects