# Import numpy for mathematical operations and calculations
import numpy as np  # Used for calculating mean of marks and other numerical operations


# Class representing a single student with their academic performance data
class Student:
    # Method to validate that marks are valid numbers within the acceptable range (0-100)
    def validate_marks(self, mark, subject):
        try:
            # Convert the mark to a float to handle both string and numeric inputs
            mark = float(mark)
            
            # Check if the mark is within the valid range (0 to 100)
            if not (0 <= mark <= 100):
                raise ValueError(f"{subject} mark must be between 0 and 100")
            
            # Return the validated mark as a float
            return mark
        except ValueError as e:
            # Re-raise with more descriptive error message including subject name
            raise ValueError(f"Invalid {subject} mark: {e}")

    # Constructor to initialize a student with their basic info and academic marks
    def __init__(self, roll_no, name, math, science, english):
        self.roll_no = roll_no  # Student's unique roll number/ID
        self.name = name        # Student's full name
        
        # Validate and store marks for each subject (ensures data integrity)
        self.math = self.validate_marks(math, "Math")        # Math marks (0-100)
        self.science = self.validate_marks(science, "Science")  # Science marks (0-100)
        self.english = self.validate_marks(english, "English")  # English marks (0-100)
        
        # Calculate derived values based on the validated marks
        self.gpa = self.calculate_gpa()    # Calculate GPA on 4.0 scale
        self.grade = self.assign_grade()   # Assign letter grade based on GPA

    # Calculate GPA (Grade Point Average) on a 4.0 scale based on marks
    def calculate_gpa(self):
        # Create a list of all subject marks for calculation
        marks = [self.math, self.science, self.english]
        
        # Calculate the average percentage across all subjects
        percentage = np.mean(marks)
        
        # Convert percentage to 4.0 GPA scale (divide by 25)
        # 100% = 4.0 GPA, 75% = 3.0 GPA, 50% = 2.0 GPA, etc.
        return round(percentage / 25, 2)

    # Assign letter grade based on calculated GPA using standard grading scale
    def assign_grade(self):
        # Grade assignment based on GPA thresholds:
        if self.gpa >= 3.5:     # 87.5% and above
            return "A"          # Excellent performance
        elif self.gpa >= 3.0:   # 75% to 87.4%
            return "B"          # Good performance
        elif self.gpa >= 2.0:   # 50% to 74.9%
            return "C"          # Satisfactory performance
        else:                   # Below 50%
            return "D"          # Needs improvement