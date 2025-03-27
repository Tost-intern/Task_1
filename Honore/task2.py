import csv

class Student:
    def __init__(self, name, math, physics, geography):
        self.name = name
        self.math = math
        self.physics = physics
        self.geography = geography

    def calculate_average(self):
        # Calculates the average of the three subjects
        return (self.math + self.physics + self.geography) / 3

    def calculate_percentage(self):
        # Calculates the percentage out of 300 (total marks in three subjects)
        total_marks = self.math + self.physics + self.geography
        return (total_marks / 300) * 100

# Function to get input and process student details
def process_students_data():
    # Ask for the number of students
    num_students = int(input("Enter the number of students: "))
    
    students = []
    
    # Take input for each student
    for _ in range(num_students):
        name = input("\nEnter the student's name: ")
        math = float(input("Enter marks for Math: "))
        physics = float(input("Enter marks for Physics: "))
        geography = float(input("Enter marks for Geography: "))
        
        student = Student(name, math, physics, geography)
        
        # Calculate average and percentage for the student
        average = student.calculate_average()
        percentage = student.calculate_percentage()
        
        # Display the results
        print(f"\nStudent: {student.name}")
        print(f"Average Marks: {average}")
        print(f"Percentage: {percentage}%\n")
        
        # Save student data to the list
        students.append([student.name, student.math, student.physics, student.geography, average, percentage])
    
    # Save the student details to a CSV file
    save_to_csv(students)

# Function to save the student data into a CSV file
def save_to_csv(students):
    with open('students_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(["Name", "Math", "Physics", "Geography", "Average", "Percentage"])
        
        # Write student data
        for student in students:
            writer.writerow(student)
    
    print("\nStudent data has been saved to 'students_data.csv'.")

# Run the program
process_students_data()
