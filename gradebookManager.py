names = ["Kyle", "Ed", "Stuart"]
Kyle_grades = [90, 83, 70]
Ed_grades = [80, 80, 75]
Stuart_grades = [98, 70, 98]
gradebook = {"Kyle" : Kyle_grades, "Ed" : Ed_grades, "Stuart" : Stuart_grades}

def average(student):
    total = 0
    for l in student:
        total += l
    average = total / len(student)
    return average


while True:
    action = input("Add student, Add grades, View gradebook, end ")
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

    elif action == "VIEW GRADEBOOK":
        for l in names:
            print(l + ": " + str(gradebook[l]) + " Average: " + str(int(average(gradebook[l]))))


    elif action == "END":
        break
