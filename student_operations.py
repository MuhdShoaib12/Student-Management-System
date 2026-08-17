from datetime import datetime
from config import SUBJECTS,MAX_MARKS,MIN_MARKS,PASSING_MARKS
from grade_calculator import calculate_grade,get_result_status,calculate_percentage

#create the student 
def create_student(roll_no,name,student_class,marks):
    total, percentage = calculate_percentage(marks)

    return {
        "roll_no":roll_no.upper(),
        "name":name.title(),
        "class":student_class.upper(),
        "marks":marks,
        "total":total,
        "percentage":percentage,
        "grade":calculate_grade(percentage),
        "result":get_result_status(marks),
        "created_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def add_student(students):
    roll_no = input("Roll Number: ").strip().upper()

    if not roll_no:
        print("Roll no cannot be empty.")
        return

    if any(s["roll_no"]==roll_no for s in students):
        print(f"Roll No '{roll_no}' already exists.")
        return
    name = input("Enter the name: ").strip()
    student_class = input("Enter the class: ").strip().upper()
    marks = {}
    print(f"Enter marks ({MIN_MARKS}-{MAX_MARKS}) for each subject:")
    for subject in SUBJECTS:
        while True:
            try:
                value = int(input(f"  {subject}: "))
                if MIN_MARKS <= value <= MAX_MARKS:
                    marks[subject] = value; break
                else:
                    print(f"  Must be between {MIN_MARKS} and {MAX_MARKS}")
            except ValueError:
                print("  Enter a valid number")

    student = create_student(roll_no, name, student_class, marks)
    students.append(student)
    print(f"Added: {student['name']} | {student['percentage']}% | {student['grade']} | {student['result']}")