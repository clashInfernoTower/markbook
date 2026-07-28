from pprint import pprint

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
    #returns a string that says what the lowest grade is and who it belongs to
    if

	return f"The lowest grade is: {min(list(markbook.values()))} which belongs to: {list(markbook.items())[list(markbook.values()).index(min(list(markbook.values())))][0]}"

def highest(markbook):
	#returns a string that says what the highest grade is and who it belongs to
	return f"The highest grade is: {max(list(markbook.values()))} which belongs to: {list(markbook.items())[list(markbook.values()).index(max(list(markbook.values())))][0]}"


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
				for x, y in markbook.items():
					print(f"{x}: {y}")
				adding_records = False
			case _:
				print("\nInput either add or stop [1]\n")
	print(average(markbook))
	print(lowest(markbook))
	print(highest(markbook))
main()
