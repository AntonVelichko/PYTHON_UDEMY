
##########################################################################################################################
###  exercise Grading  ###

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding" 
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)

---

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
def score_to_grade(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceeds Expectations"
    elif score > 70:
        return "Acceptable"
    else:
        return "Fail"
 
student_grades = {}
 
for key in student_scores:
    student_grades[key] = score_to_grade(student_scores[key])




[end]
