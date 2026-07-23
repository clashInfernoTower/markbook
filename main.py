markbook = {}

def add_records(markbook):
    x = True
    y = True
    while x:
        name = input("Input the student's name: ")
        if name:
            x = False
        else:
            print("Name cannot be empty: ")

    while y:
        try: 
            score = int(input("Input the student's score\n(Must be between 0 and 100 and cannot be empty): "))
            if score:
            
            else:
                print("Score needs to be a whole number!: ")
        except ValueError:
            print("Score needs to be a whole number: ")
