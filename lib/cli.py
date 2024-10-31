import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Team, Player

def main():
    engine = create_engine("sqlite:///football.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\nWelcome to the Football Management System!")
        print("1. Manage Teams")
        print("2. Manage Players")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_teams(session)
        elif choice == '2':
            manage_players(session)
        elif choice == '3':
            print("Exiting the application...")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Please enter a number.")

def manage_teams(session):
    while True:
        print("\nTeam Management Menu:")
        print("1. Create Team")
        print("2. Display All Teams")
        print("3. Find Team by ID")
        print("4. Delete Team")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter team name: ")
            city = input("Enter team city: ")
            stadium = input("Enter team stadium: ")
            team = Team.create(session, name, city, stadium)
            print("Team created successfully!", team)
        elif choice == '2':
            print("\nAll Teams:")
            teams = Team.get_all(session)
            for team in teams:
                print(team)
        elif choice == '3':
            try:
                id = int(input("Enter team ID: "))
                team = Team.find_by_id(session, id)
                if team:
                    print(team)
                else:
                    print("Team not found.")
            except ValueError:
                print("Invalid input. Please enter a valid team ID.")
        elif choice == '4':
            try:
                id = int(input("Enter team ID: "))
                team = Team.find_by_id(session, id)
                if team:
                    team.delete(session)
                    print("Team deleted successfully!")
                else:
                    print("Team not found.")
            except ValueError:
                print("Invalid input. Please enter a valid team ID.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number.")

def manage_players(session):
    while True:
        print("\nPlayer Management Menu:")
        print("1. Create Player")
        print("2. Display All Players")
        print("3. Find Player by ID")
        print("4. Delete Player")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter player name: ")
            position = input("Enter player position: ")

            # Validate team ID
            while True:
                try:
                    team_id = int(input("Enter team ID: "))
                    team = Team.find_by_id(session, team_id)
                    if team:
                        break
                    else:
                        print("Invalid team ID. Please enter a valid team ID.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            player = Player.create(session, name, position, team_id)
            print("Player created successfully!", player)
        elif choice == '2':
            print("\nAll Players:")
            players = Player.get_all(session)
            for player in players:
                print(player)
        elif choice == '3':
            id = int(input("Enter player ID: "))
            player = Player.find_by_id(session, id)
            if player:
                print(player)
            else:
                print("Player not found.")
        elif choice == '4':
            id = int(input("Enter player ID: "))
            player = Player.find_by_id(session, id)
            if player:
                player.delete(session)
                print("Player deleted successfully!")
            else:
                print("Player not found.")
        elif choice == '5':
            break        
        else:
            print("Invalid choice. Please enter a number.")


if __name__ == "__main__":
    main()
