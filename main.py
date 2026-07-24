markbook = {}

def add_records(markbook):
    add_student = True
    add_score = True
    
    while add_student == True:
        name = input("Input the student's name: ")
        if name:
            add_student = False
        else:
            print("Name cannot be empty: ")

    while add_score == True:
        try: 
            score = int(input("Input the student's score\n(Must be between 0 and 100 and cannot be empty): "))
            if score:
                match score:
                    case int() if score > 0 and score < 100:
                        markbook.update(Student=name, Score=score)
                        add_score = False
                        
            else:
                print("Score needs to be a whole number!: ")
        except ValueError:
            print("Score needs to be a whole number: ")
    print(markbook)


add_records(markbook)
