import json
from datetime import date

# functions

habits = {

}
def showlist(habits):
    print("this is the list of habits")
    print(habits)

def load_habits():
    try:
        with open('habits.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
habits = load_habits()

def save_habits(habits):  
    with open("habits.json", 'w') as f:
        json.dump(habits, f)




def remove_habit(habits):
    removehabit = input(f"remove a habit: {habits}")
    if removehabit not in habits:
        print(f"please remove among the options: {habits}")
    else:
        del habits[removehabit]
        print(f"removed {removehabit} from the list of habits")
    

def add_habit(habits):
    addedhabit = input("add a habit: ").strip()
    if addedhabit in habits:
        print("habit name already exists")
    else:
        habits[addedhabit] = [str(date.today())]
        print(f"the habit: {addedhabit} is added.")
    
        
    


# adding the different options

def main():
    while True:    
        print("Habit Tracker")
        print("1. Add a habit")
        print("2. Remove a habit")
        print("3. View your habits")
        print("4. Save your habit")
        print("5. Exit the program")

        options = input("please select one of the options: ")

        if options == "1":
            print(add_habit(habits))
        elif options == "2":
            print(remove_habit(habits))
        elif options == "3":
            print(showlist(habits))
        elif options == "4":
            choiceinput = input("save? yes or no: ").lower()
            if choiceinput == "yes":
                save_habits(habits)
            elif choiceinput == "no":
                print("cancelling")

            
        elif options == "5":
            print("Thank You and Goodbye")
            break
        else:
            print("please input a number")


if __name__ == "__main__":
    main()