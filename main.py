markbook = {}
final_grades = {}

def add_records(markbook):
    add_student = True
    add_score = True
    
    #Allows the user to input a student's name again if they accidentally made it empty.
    while add_student == True:
        name = input("Input the student's name: ")
        if name:
            add_student = False
        else:
            print("\nName cannot be empty\n")

    #Allows the user to input a student's score again if they accidentally make it empty or less than zero or more than 100
    while add_score == True:
        try: 
            score = int(input("Input the student's score\n(Must be between 0 and 100 and cannot be empty): "))
            if score:
                match score:
                    case int() if score >= 0 and score <= 100:
                        markbook[name] = score
                        add_score = False
                    case _:
                        print("The score cannot be less than zero and more than 100\n")
                        
            else:
                print("\nScore needs to be a whole number!\n")
        except ValueError:
            print("\nScore needs to be a whole number\n")
    
    return
    


def average(markbook):
    return f"The average grade is: {sum(list(markbook.values())) / len(list(markbook.values()))}"

def lowest(markbook):
    lowest_scored_students = []
    students = list(markbook.items())
    students.sort(key=lambda score: score[1])
    
    for student, score in students:
        if score == students[0][1]:
            lowest_scored_students.append(student)
    
    #Makes the lowest scored_students nicer to read
    simplified_lowest_scored_students = ", ".join(student for student in lowest_scored_students)
    #returns a string that says what the lowest grade is and who it belongs to, multiple people can have the same lowest score which the code above in this function allows
    return f"The lowest grade is: {students[0][1]} which belongs to: {simplified_lowest_scored_students}"


def highest(markbook):
    highest_scored_students = []
    students = list(markbook.items())
    students.sort(key=lambda score: score[1], reverse=True)
    
    for student, score in students:
        if score == students[0][1]:
            highest_scored_students.append(student)

    #Makes the highest_scored_students nicer to read
    simplified_highest_scored_students = ", ".join(student for student in highest_scored_students)
    #returns a string that says what the highest grade is and who it belongs to, multiple people can have the same highest score which the code above in this function allows
    return f"The highest grade is: {students[0][1]} which belongs to: {simplified_highest_scored_students}"

def grade(markbook):
    for student, score in list(markbook.items()):
        match score:
            case score if score >= 90:
                final_grades[student] = 'E'
            case score if score >= 70:
                final_grades[student] = 'M'
            case score if score >= 50:
                final_grades[student] = 'A'
            case _:
                final_grades[student] = 'NA'
    
    formatted_final_grade = ""
    for student, grade in list(final_grades.items()):
        formatted_final_grade += f"--{student} : {grade}\n"
    return f"The final grades are:\n\n{formatted_final_grade}"

def main():
    adding_records = True
    #Gives the user the opportunity to add records and stop whenever they need to
    while adding_records:
        ask = input("Do you want to add records or stop?\n[add / stop]: ")
        match ask:
            case 'add':
                add_records(markbook)   
            case 'stop':
                if not markbook:
                    print("\nThere is nothing in the markbook\n")
                    return
                for name, score in markbook.items():
                    print(f"{name}: {score}")
                adding_records = False
            case _:
                print("\nInput either add or stop [1]\n")
    print(average(markbook))
    print(lowest(markbook))
    print(highest(markbook))
    print(grade(markbook))
main()
