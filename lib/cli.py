from models import session, User, FitnessGoal, Progress
from helpers import (
    exit_program,
    add_new_user,
    add_fitness_goal,
    track_progress,
    view_fitness_goals,
    view_goal_progress,
    delete_fitness_goal
)

def main():
    while True:
        menu()
        choice = input("> ").strip()
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_new_user()
        elif choice == "2":
            add_fitness_goal()
        elif choice == "3":
            track_progress()
        elif choice == "4":
            view_fitness_goals()
        elif choice == "5":
            view_goal_progress()
        elif choice == "6":
            delete_fitness_goal()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\n--- Fitness Goal Tracker ---")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new user")
    print("2. Create a fitness goal")
    print("3. Track progress")
    print("4. View all fitness goals for a user")
    print("5. View progress for a specific fitness goal")
    print("6. Delete a fitness goal")

if __name__ == "__main__":
    main()
