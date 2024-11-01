import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import League, Team, Player

def main():
    engine = create_engine("sqlite:///football.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\nWelcome to the Football Management System!")
        menu_options = {
            "1": "Manage Leagues",
            "2": "Manage Teams",
            "3": "Manage Players",
            "4": "Exit"
        }

        for key, option in menu_options.items():
            print(f"{key}. {option}")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_leagues(session)
        elif choice == '2':
            manage_teams(session)
        elif choice == '3':
            manage_players(session)
        elif choice == '4':
            print("Exiting the application...")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Please enter a number.")

def manage_leagues(session):
    while True:
        print("\nLeague Management Menu:")
        options = [
            ("1", "Create League"),
            ("2", "Display All Leagues"),
            ("3", "Find League by ID"),
            ("4", "Delete League"),
            ("5", "Back to Main Menu")
        ]

        for key, option in options:
            print(f"{key}. {option}")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter league name: ")
            country = input("Enter league country: ")
            league = League.create(session, name, country)
            print("League created successfully!", league)
        elif choice == '2':
            leagues = League.get_all(session)
            display_leagues(leagues)
        elif choice == '3':
            id = int(input("Enter league ID: "))
            league = League.find_by_id(session, id)
            print(league if league else "League not found.")
        elif choice == '4':
            id = int(input("Enter league ID: "))
            league = League.find_by_id(session, id)
            if league:
                league.delete(session)
                print("League deleted successfully!")
            else:
                print("League not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number.")

def display_leagues(leagues):
    if leagues:
        print("\nAll Leagues:")
        for league in leagues:
            print(league)
    else:
        print("No leagues found.")

def manage_teams(session):
    while True:
        print("\nTeam Management Menu:")
        options = [
            ("1", "Create Team"),
            ("2", "Display All Teams"),
            ("3", "Find Team by ID"),
            ("4", "Delete Team"),
            ("5", "Back to Main Menu")
        ]

        for key, option in options:
            print(f"{key}. {option}")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter team name: ")
            city = input("Enter team city: ")
            stadium = input("Enter team stadium: ")
            league_id = int(input("Enter league ID for the team: "))
            team = Team.create(session, name, city, stadium, league_id)
            print("Team created successfully!", team)
        elif choice == '2':
            teams = Team.get_all(session)
            display_teams(teams)
        elif choice == '3':
            id = int(input("Enter team ID: "))
            team = Team.find_by_id(session, id)
            print(team if team else "Team not found.")
        elif choice == '4':
            id = int(input("Enter team ID: "))
            team = Team.find_by_id(session, id)
            if team:
                team.delete(session)
                print("Team deleted successfully!")
            else:
                print("Team not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number.")

def display_teams(teams):
    if teams:
        print("\nAll Teams:")
        for team in teams:
            print(team)
    else:
        print("No teams found.")

def manage_players(session):
    while True:
        print("\nPlayer Management Menu:")
        options = [
            ("1", "Create Player"),
            ("2", "Display All Players"),
            ("3", "Find Player by ID"),
            ("4", "Delete Player"),
            ("5", "Back to Main Menu")
        ]

        for key, option in options:
            print(f"{key}. {option}")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team_id = int(input("Enter team ID: "))
            player = Player.create(session, name, position, team_id)
            print("Player created successfully!", player)
        elif choice == '2':
            players = Player.get_all(session)
            display_players(players)
        elif choice == '3':
            id = int(input("Enter player ID: "))
            player = Player.find_by_id(session, id)
            print(player if player else "Player not found.")
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

def display_players(players):
    if players:
        print("\nAll Players:")
        for player in players:
            print(player)
    else:
        print("No players found.")

if __name__ == "__main__":
    main()
