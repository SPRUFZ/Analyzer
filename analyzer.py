# Name: lukka 
# Period:pm
# Student Performance Analyzer
#program intro
print("========================================")
print("      STUDENT PERFORMANCE ANALYZER")
print("========================================")
# all my variables that i use 
name = input("what is the students name:")

grade = int(input("what grade level is the student in:"))

assignment_average = float(input("What is the student's assignment average:"))

quiz_average = float(input("What is the student's quiz average:"))

test_average = float(input("What is the student's test average:"))

attendence = float(input("What is the student's attendance percentage:"))

missing = int(input("How many missing assignments does the student have:"))
#def to see overall grade using the other variables
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40
    overall_grade = assignment_portion + quiz_portion + test_portion
    return overall_grade 

overall_grade = calculate_grade(assignment_average, quiz_average, test_average)
print(f"Overall grade: {overall_grade}")
#more defs using variables to see letter grade, attendence, and missing assignments
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
# def to check for attendence and displays message based on answer
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
# def to check how many assignments student is missing and displays a message according to the amount
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
#nested def to find elegibilty for academics
def check_eligibility(overall_grade, attendence, missing):
    if overall_grade >= 70:
        if attendence >= 90:
            if missing <= 2:
                 print(f"Academic Eligibility: ELIGIBLE. Student passed all three requirements.")
            else:
                print(f"Academic Eligibility: NOT ELIGIBLE. Reason: Too many missing assignments.")
        else:
            print(f"Academic Eligibility: NOT ELIGIBLE. Reason: Attendance is too low.")
    else:
        print(f"Academic Eligibility: NOT ELIGIBLE. Reason: Overall grade is too low.")        

check_eligibility(overall_grade, attendence, missing)
# one more nested def to check for high honors
def check_high_honors(overall_grade, attendence, missing):
    if overall_grade >= 90:
        if attendence >= 95:
            if missing == 0:
                print(f"High Honors: YES.")
            else:
                print(f"High Honors: NO. Reason: Student has missing assignments.")
        else:
            print(f"High Honors: NO. Reason: Attendance requirement not met.")
    else:
        print(f"High Honors: NO. Reason: Grade requirement not met.")

check_high_honors(overall_grade, attendence, missing)

def check_good_standing(overall_grade, attendence):
    if overall_grade >= 70 and attendence >= 90:
        print(f"Good standing: YES")
    else:
        print(f"Good standing: NO")


check_good_standing(overall_grade, attendence)

def check_support(overall_grade, attendence):
    if overall_grade < 70 or attendence < 80:
        print(f"Additional Support: RECOMMENDED")
    else:
        print(f"Additional Support: NOT NEEDED")

check_support(overall_grade, attendence)


user = input("enter username:")
pin = input("enter pin:")

real_user = "student"
real_pin = "1234"
#small nest to make sure the student has thev right user and pin in order
if user == real_user:
    if pin == real_pin:
        print(f"login succesfull.")
    else:
        print(f"login failed: Incorrect PIN.")
else:
    print(f"login failed: incorrect username.")


def grade_level_message(grade):
    if grade == 9:
        print(f"welcome to your freshman year!!")
    elif grade == 10:
        print(f"keep building your skills!!")
    elif grade == 11:
        print(f"Junior year - KEEP PUSHINGGGGG")
    elif grade == 12:
        print(f"Senior year - finish strong unc")
    else:
        print(f"Invalid Grade Level")

def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average and assignment_average >= test_average:
        print(f"Strongest category: Assignments")
    elif quiz_average >= assignment_average and quiz_average >= test_average:
        print(f"Strongest category: Quizzes")
    else:
        print(f"Strongest category: Tests")

strongest_category(assignment_average, quiz_average, test_average)
#extra credit def to check if they are a standard or outstanding student
def check_advanced_status(overall_grade, attendence, missing):
        if (overall_grade >= 90 and attendence >= 95) or (overall_grade >= 85 and missing == 0):
                print("Advanced Status: OUTSTANDING STUDENT")
        else:
                print("Advanced Status: STANDARD STUDENT STATUS")

# final summary for student showing final scores for everything personalized to the inputs of the student
print("========================================")
print("             STUDENT SUMMARY")
print("========================================")
print(f"Name: {name}")
print(f"Grade Level: {grade}")
print(f"Assignment Average: {assignment_average}%")
print(f"Quiz Average: {quiz_average}%")
print(f"Test Average: {test_average}%")
print(f"Overall Grade: {overall_grade:.2f}%")
print(f"Attendance: {attendence}%")
print(f"Missing Assignments: {missing}")
check_advanced_status(overall_grade, attendence, missing)
print("========================================")





