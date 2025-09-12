def average(student):
    total = 0
    for l in student:
        total += l
    average = total / len(student)
    return int(average)

def letter(grade):
    if grade >= 90:
        return("A")
    elif grade >= 80:
        return("B")
    elif grade >= 70:
        return("C")
    elif grade >= 60:
        return("D")
    else:
        return("F")
    

names = ["Kyle", "Ed", "Stuart"]
Kyle_grades = [90, 83, 70]
Ed_grades = [80, 80, 75]
Stuart_grades = [98, 70, 98]
gradebook = {"Kyle" : Kyle_grades, "Ed" : Ed_grades, "Stuart" : Stuart_grades}
averages = {"Kyle" : average(Kyle_grades), "Ed" : average(Ed_grades), "Stuart" : average(Stuart_grades)}


while True:
    action = input("Add student, Add grades, View gradebook, Remove student, Remove grade, end ")
    action = action.upper()
    if action == "ADD STUDENT":
        name = input("What is the student's name? ")
        name = name.capitalize()
        names.append(name)
        grades_amount = int(input("How many grades does this student have? "))
        grades = []
        for i in range(grades_amount):
            grade = int(input("Enter Grade: "))
            grades.append(grade)
        gradebook[name] = grades
        averages[name] = average(grades)

    elif action == "ADD GRADES" :
        student = input("What student would you like to add a grade to? ")
        student = student.capitalize()
        if student in names:
            grade = int(input("Input Grade: "))
            gradebook[student].append(grade)
            averages [student] = average(gradebook[student])
            break
        else:
            print("Name not in gradebook, please try again")


    elif action == "VIEW GRADEBOOK":
        averages = dict(sorted(averages.items(), key = lambda item: item[1]))
        averages = dict(reversed(list(averages.items())))
        for l in averages:
            print(l + ":" + str(gradebook[l]) + " Average: " + str(average(gradebook[l])) + " " + letter(average(gradebook[l])))
        print("Top Student: " + max(averages))

    elif action == "REMOVE STUDENT":
        student = input("What student would you like to remove? ")
        student = student.capitalize()
        if student in names:
            names.remove(student)
            del gradebook[student]
            del averages[student]
        else:
            print("Student not in gradebook, please try again.")
    elif action == "REMOVE GRADE":
        student = input("What student would you like to remove a grade from? ")
        student = student.capitalize()
        if student in names:
            print(student + "'s Grades: " + str(gradebook[student]))
            grade_to_remove = int(input("Which grade would you like to remove"))
            if grade_to_remove in gradebook[student]:
                gradebook[student].remove(grade_to_remove)
            else:
                print("Not one of student's grades please try again")
        else:
            print("Name not in gradebook, please try again")


    elif action == "END":
        break