markbook = {}

def add_records(markbook):
    add_student = True
    add_score = True
    
    #Allows the user to input a student's name again if they accidentally made it empty.
    while add_student == True:
        name = input("Input the student's name: ")
        if name:
            add_student = False
        else:
            print("Name cannot be empty: ")

    #Allows the user to input a student's score again if they accidentally make it empty or less than zero or more than 100
    while add_score == True:
        try: 
            score = int(input("Input the student's score\n(Must be between 0 and 100 and cannot be empty): "))
            if score:
                match score:
                    case int() if score >= 0 and score <= 100:
                        markbook.update(Student=name, Score=score)
                        add_score = False
                    case _:
                        print("The score cannot be less than zero and more than 100")
                        
            else:
                print("Score needs to be a whole number!")
        except ValueError:
            print("Score needs to be a whole number")
    print(markbook)


def average(markbook):
    return sum(list(markbook.values())) / len(list(markbook.values()))



def main():
    add_records(markbook)
    average(markbook)
