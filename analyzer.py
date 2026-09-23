# Name: lukka 
# Period:pm
# Student Performance Analyzer
#program intro
print("========================================")
print("      STUDENT PERFORMANCE ANALYZER")
print("========================================")

name = input("what is the students name:")

grade = int(input("what grade level is the student in:"))

assignment_average = float(input("What is the student's assignment average:"))

quiz_average = float(input("What is the student's quiz average:"))

test_average = float(input("What is the student's test average:"))

attendence = float(input("What is the student's attendance percentage:"))

missing = int(input("How many missing assignments does the student have:"))

def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40
    overall_grade = assignment_portion + quiz_portion + test_portion
    return overall_grade 

overall_grade = calculate_grade(assignment_average, quiz_average, test_average)
print(f"Overall grade: {overall_grade}")

def letter_grade(overall_grade):
    if overall_grade >= 90:
        print(f"Letter grade: A")
    elif overall_grade >= 80:
        print(f"Letter grade: B")
    elif overall_grade >=70:
        print(f"Letter grade: C")
    elif overall_grade >= 60:
        print(f"Letter grade: D")
    else:
        print(f"Letter grade: F")
        return 
letter_grade(overall_grade)

def attendence_status(attendence):
    if attendence >= 95:
        print(f"Excellent Attendence")
    elif attendence >= 90:
        print(f"Good attendence")
    elif attendence >=80:
        print(f"Attendence warning")
    else:
        print(f"poor attendence")
        return 
attendence_status(attendence)

def missing_assignment_status(missing):
    if missing == 0:
        print(f"Missing assignment status: excellent")
    elif missing <= 2:
        print(f"Missing assignment status: good")
    elif missing <= 4:
        print(f"Missing assignment status: warning")
    else:
        print(f"Missing assignment status: CRITICAL")

missing_assignment_status(missing)

def check_eligibility(overall_grade, attendence, missing_assignments):
    if overall_grade <= 69:
        print(f"Academic Eligibility: NOT ELIGIBLE. Reason: Overall grade is too low.")
    if attendence >= 90:
        print(f"Academic Eligibility: NOT ELIGIBLE. Reason: Attendance is too low.")
    if missing <= 2