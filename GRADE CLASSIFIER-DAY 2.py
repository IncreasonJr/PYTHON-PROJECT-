def average():
    sum_of_marks=sum(marks)
    number_of_marks=len(marks)
    average=sum_of_marks/number_of_marks
    return average


def grade():
    if average>= 80 and average<=100:
       print(" grade is A")
    elif average>= 60 and int(average)< 80:
        print("grade is B")
    elif average>=50 and int(average)<60:
        print("grade is C")
    else:
        print("grade is F")
    return grade 

marks=[101]
average=average()
print(f'The average  of {sum(marks)} is ' + str(average))
grade=grade()