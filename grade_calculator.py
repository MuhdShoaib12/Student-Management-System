from config import PASSING_MARKS,GRADE_THRESHOLDS

#Calculateing the grade based on the percentage
def calculate_grade(percentage):
    for grade, threshold in GRADE_THRESHOLDS.items():
        if percentage >= threshold:
            return grade

        return "F"

#Getting student result status baased on the marks obtained
def get_result_status(marks_dict):
    for marks in marks_dict.values():
        if marks < PASSING_MARKS:
            return "Fail"

        return "Pass"

#getting the percentage of obtained by the student
def calculate_percentage(marks_dict,max_per_subject = 100):
    total = sum(marks_dict.values())
    percentage = round((total / (len(marks_dict) * max_per_subject)) * 100, 2)
    return total, percentage
    
    

        