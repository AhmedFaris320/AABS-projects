# Import required libraries for data visualization
import matplotlib.pyplot as plt  # For creating basic plots and charts
import seaborn as sns  # For advanced statistical data visualization


# Function to create and save a bar chart showing average marks per subject
def save_avg_subject_chart(df, path):
	# Calculate the mean (average) marks for math, science, and english columns
	avg_per_subject = df[["math","science","english"]].mean()
	
	# Create a new figure and axis for the plot
	fig, ax = plt.subplots()
	
	# Create a bar chart with different colors for each subject
	# skyblue for math, lightgreen for science, salmon for english
	avg_per_subject.plot(kind="bar", color=["skyblue","lightgreen","salmon"], ax=ax)
	
	# Save the figure to the specified file path
	fig.savefig(path)
	
	# Close the figure to free up memory
	plt.close(fig)


# Function to create and save a line chart showing GPA trend by roll number
def save_gpa_trend_chart(df, path):
	# Create a new figure and axis for the plot
	fig, ax = plt.subplots()
	
	# Plot a line chart with roll_no on x-axis and GPA on y-axis
	# marker="o" adds circular markers at each data point
	# color="purple" sets the line color to purple
	ax.plot(df["roll_no"], df["GPA"], marker="o", color="purple")
	
	# Save the figure to the specified file path
	fig.savefig(path)
	
	# Close the figure to free up memory
	plt.close(fig)


# Function to create and save a correlation heatmap showing relationships between subjects and GPA
def save_heatmap(df, path):
	# Create a new figure and axis for the plot
	fig, ax = plt.subplots()
	
	# Calculate correlation matrix between math, science, english, and GPA
	# This shows how strongly each subject correlates with others and with GPA
	corr = df[["math","science","english","GPA"]].corr()
	
	# Create a heatmap using seaborn
	# annot=True displays correlation values on each cell
	# cmap="coolwarm" uses a blue-to-red color scheme (cool to warm colors)
	sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
	
	# Save the figure to the specified file path
	fig.savefig(path)
	
	# Close the figure to free up memory
	plt.close(fig)


# Function to create and save a bar chart showing the distribution of grades
def save_grade_distribution(df, path):
	# Create a new figure and axis for the plot
	fig, ax = plt.subplots()
	
	# Create a count plot (bar chart) showing how many students got each grade
	# x="Grade" means the x-axis shows different grades (A, B, C, D)
	# data=df specifies the DataFrame to use
	# palette="Set2" uses a predefined color palette for different bars
	sns.countplot(x="Grade", data=df, palette="Set2", ax=ax)
	
	# Save the figure to the specified file path
	fig.savefig(path)
	
	# Close the figure to free up memory
	plt.close(fig)