import math

def calculate_average(marks):
    if len(marks) != 3:
        print("Missing marks")
        return None

    for x in marks:
        if x < 0 or x > 100:
            print("Negative marks or marks exceeding 100")
            return None

    Average = sum(marks)/3
    return Average

def classify_performance(average):
    if average == None:
        return None

    if average >= 80:
        print("Excellent")
    elif average >= 70:
        print("Good")
    elif average >= 60:
        print("Satisfactory") 
    else:
        print("Needs Improvement")

def display_report(students):
    for x in students:
        average = calculate_average(x[2])
        if average == None:
            print(x[0], x[1], "Invalid marks")
        else:    
            print(x[0], x[1], average, end = " ")
            classify_performance(average)
            

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]
display_report(students)

equal = [[201, "Aryan", [90, 90, 90]]]
display_report(equal)

invalid = [[201, "Aryan", [-90, 90, 90]]]
display_report(invalid)

miss = [[201, "Aryan", [67, 67]]]
display_report(miss)