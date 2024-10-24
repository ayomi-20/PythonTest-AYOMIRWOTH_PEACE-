# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
def student_grading_system():
    student_mark = int(input("Enter the mark you scored: "))
    if student_mark >= 90 and student_mark <= 100:
        print("The student grade you obtained is A")
    elif student_mark >= 80 and student_mark <= 89:
        print("The student grade you obtained is B")
    elif student_mark >= 70 and student_mark <= 79:
        print("The student grade you obtained is C")
    elif student_mark >= 60 and student_mark <= 69:
        print("The student grade you obtained is D")
    elif student_mark >= 40 and student_mark <= 59:
        print("The student grade you obtained is E")
    else:
        print("The student grade you obtained is F")
student_grading_system()