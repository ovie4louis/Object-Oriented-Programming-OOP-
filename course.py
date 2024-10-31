class Course:
    number_students = 5  # Class variable to keep track of available student registration slots (maximum 5 allowed)

    def __init__(self, name, course, units):
        # Initialize instance attributes for the student's name, course, and units
        self.name = name
        self.course = course
        self.units = units

    def student_name(self):
        # Returns the student's name
        return self.name

    def student_course(self):
        # Returns the student's course
        return self.course

    def student_units(self):
        # Returns the number of units for the student's course
        return self.units

    def student_name_course_unit(self):
        # Returns a tuple containing the student's name, course, and units
        return self.name, self.course, self.units

    def register_course(self):
        # Registers a student if slots are available (number_students > 0)
        if Course.number_students > 0:
            Course.number_students -= 1  # Decrement the class variable by 1 to register the student
            return self.student_name_course_unit()  # Return student's details
        else:
            # If maximum registrations reached, return a message
            return "Maximum number reached"

# Testing the class with multiple students
student1 = Course("ovie", "PHY101", 3)
student2 = Course("paul", "BIO101", 2)
student3 = Course("peace", "MATH101", 1)
student4 = Course("joy", "CHM101", 3)
student5 = Course("louis", "GEO101", 1)
student6 = Course("James", "FUR104", 3)

# Registering each student and printing the results
print(student1.register_course())  # Expected output: ('ovie', 'PHY101', 3)
print(student2.register_course())  # Expected output: ('paul', 'BIO101', 2)
print(student3.register_course())  # Expected output: ('peace', 'MATH101', 1)
print(student4.register_course())  # Expected output: ('joy', 'CHM101', 3)
print(student5.register_course())  # Expected output: ('louis', 'GEO101', 1)
print(student6.register_course())  # Expected output: "Maximum number reached" as limit is exceeded
