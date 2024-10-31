# Course Registration System

This project implements a simple `Course` class to manage student registrations for a course. The class has a maximum limit of 5 students who can register, and it tracks available registration slots. Each student has a name, course, and unit count associated with them. The registration system prevents any student from registering if the slot limit is exceeded.

## Class Structure

### Class Variable
- `number_students`: Tracks available slots for student registration. This is a class-level variable, shared among all instances, and is initialized to `5`.

### Constructor
- `__init__(self, name, course, units)`: Initializes each student's name, course, and unit count.

### Instance Methods
- `student_name(self)`: Returns the student's name.
- `student_course(self)`: Returns the student's course.
- `student_units(self)`: Returns the number of units for the student's course.
- `student_name_course_unit(self)`: Returns a tuple with the student's name, course, and units.
- `register_course(self)`: Registers a student if slots are available (`number_students > 0`). Decrements the slot count by 1 if registration is successful, returning the student's details. If the registration limit is reached, it returns a message `"Maximum number reached"`.

## Usage Example

```python
# Creating instances of Course for multiple students
student1 = Course("ovie", "PHY101", 3)
student2 = Course("paul", "BIO101", 2)
student3 = Course("peace", "MATH101", 1)
student4 = Course("joy", "CHM101", 3)
student5 = Course("louis", "GEO101", 1)
student6 = Course("James", "FUR104", 3)

# Registering each student and printing the results
print(student1.register_course())  # Output: ('ovie', 'PHY101', 3)
print(student2.register_course())  # Output: ('paul', 'BIO101', 2)
print(student3.register_course())  # Output: ('peace', 'MATH101', 1)
print(student4.register_course())  # Output: ('joy', 'CHM101', 3)
print(student5.register_course())  # Output: ('louis', 'GEO101', 1)
print(student6.register_course())  # Output: "Maximum number reached"

