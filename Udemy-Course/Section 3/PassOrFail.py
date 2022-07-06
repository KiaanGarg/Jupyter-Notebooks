data_valid = False

while data_valid == False:
    grade1 = input("Type the grade of the first test: ")

    try:
        grade1 = int(grade1)
    except:
        print("Invalid Number")
        continue
        
    if (grade1 < 0 or grade1 > 10):
        print("Grade can't be less than 0 or greater than 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = input("Type the grade of the second test: ")

    try:
        grade2 = int(grade2)
    except:
        print("Invalid Number")
        continue
    
    if (grade2 < 0 or grade2 > 10):
        print("Grade can't be less than 0 or greater than 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    total_classes = input("Type the number of total classes: ")

    try:
        total_classes = int(total_classes)
    except:
        print("Invalid Number")
        continue
    
    if (total_classes <= 0):
        print("Total classes have to be greater than 0")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = input("Type the number of absences: ")

    try:
        absences = int(absences)
    except:
        print("Invalid Number")
        continue
    
    if (absences < 0 or absences > total_classes):
        print("Absences can't be less than 0 or greater than the total number of classes")
        continue
    else:
        data_valid = True

avg_marks = (grade1 + grade2)/2
attendance = (total_classes - absences)/total_classes

print("Average marks: ", round(avg_marks, 2))
print("Attendance rate: ", str(round(attendance * 100, 2)) + "%")

if(attendance < 0.8 and avg_marks < 6):
    print("The student has failed due to an attendance rate less than 80% and average marks less than six")
elif(attendance < 0.8):
    print("The student has failed due to an attendance rate less than 80%")
elif(avg_marks < 6):
    print("The student has failed due to average marks less than 6")
else:
    print("The student has passed")



#Error Handling Section
    
