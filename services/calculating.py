# Calculate Average GPA student
def Average_GPA(Slist):
    if not Slist:
        return 0.0

    total_gpa = sum(student.gpa for student in Slist)
    return round((total_gpa / len(Slist)), 2)


def statistics(Slist):

    classification = {"Excellent": 0, "Good": 0, "Fair": 0, "Average": 0, "Weak": 0}

    if not Slist:
        return classification

    for student in Slist:
        if student.gpa >= 3.6:
            classification["Excellent"] += 1
        elif student.gpa >= 3.2:
            classification["Good"] += 1
        elif student.gpa >= 2.5:
            classification["Fair"] += 1
        elif student.gpa >= 2.0:
            classification["Average"] += 1
        else:
            classification["Weak"] += 1

    return classification
