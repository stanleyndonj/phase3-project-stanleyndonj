
# FootyManager CLI

---

FootyManager CLI is a command-line interface (CLI) application written in Python programming language which is used for the administration of football players and teams stored in a local SQLite database. The application uses SQLalchemy to implement ORM, which simplifies the process of creating, retrieving, updating and deleting records from the database without having to write complex SQL statements. This project exemplifies the role of Python in the development of Command Line Interface, management of the database using SQLAlchemy ORM, and the practice of application design using modular structure.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Structure](#code-structure)
6. [Models Overview](#models-overview)
7. [Future Improvements](#future-improvements)

---

## Project Overview
---

Footymanager was developed CLI was developed within the frame of the project phase 3 as an attempt to learn command line interface applications, ORM, and database management. The application is perfect for a database administrator of a football club; it facilitates the efficient organization of team and player data through a simple command line interface. The database is designed to provide a means of relationship between teams and players in terms of players belonging to a team,... creating a team and seeking the roster of that team.
---

## Features

- **Team Management**:  team creation, team viewing, team finding, and team deletion.
- **Player Management**: creation of players, listing, searching, deletion, linking of the players to teams.
- **Clear and Informative CLI Prompts**: 
Organized menu-driven navigation to improve the user's experience.
- **ORM Database CRUD Operations**: Uses SQLAlchemy as a database CRUD handler.
- **Modular Code Setup**: The code consists of a number of modules wherein lie separate sections for command line interface operations, model definitions, and database reset functionality.

---

## Installation

Here how to setup FootyManager CLI and run it locally:

1. **Clone the Repository**
   ```bash
   git clone git@github.com:stanleyndonj/phase3-project-stanleyndonj.git
   cd footy-manager-cli
   ```

2. **Install Dependencies**
   - Ensure you have Python and Pipenv installed, then install dependencies:
   ```bash
   pipenv install
   ```

3. **Activate the Virtual Environment**
   ```bash
   pipenv shell
   ```

4. **Set Up the Database**
   - Run the `reset_db.py` script to initialize the database:
   ```bash
   python reset_db.py
   ```

---

## Usage

To run the application, execute the following command:

```bash
python cli.py
```

This command will launch the CLI, where you can choose from the following menus:

1. **Manage Teams**
   - Create a team with `name`, `city`, and `stadium` details.
   - List all teams in the database.
   - Search for a team by ID.
   - Delete a team by ID.

2. **Manage Players**
   - Add a player with a `name`, `position`, and team ID.
   - List all players in the database.
   - Search for a player by ID.
   - Delete a player by ID.

---

## Code Structure

- **cli.py**: Main CLI script, UI for managing players and teams.
- **models.py**: Defines the Team and Player models using SQLAlchemy ORM.
- **reset_db.py**:  A command line utility script for resetting the database which drops all tables and re-initializes them.
- **Pipfile**:  Allows you to manage your project dependencies using Pipenv.
- **README.md**:  Setup, Usage instructions, and Project description.

---

## Models Overview

- **Team**: 
   - Fields: `id`, `name`, `city`, `stadium`
   - Methods: Create a team, retrieve all teams, find by ID, and delete a team.
   - Relationships: One-to-many relationship with the `Player` model.

- **Player**: 
   - Fields: `id`, `name`, `position`, `team_id`
   - Methods: Create a player, retrieve all players, find by ID, delete a player, and retrieve the associated team.
   - Relationships: Many-to-one relationship with the `Team` model.

---

## Future Enhancements

- **Stricter Validation**:Enforce validation to disallow duplicate team names being created. 
- **Team managment**: Incorporate a player transfer system among teams.
- **Additional search criteria**: Enable search by any other fields as for example player position or team location.
- **Performance stats**: Expand the player model to feature performance stats like scores, assists, etc. 
---

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to fork the repository and make contributions to improve the project!

---

Thank you for using FootyManager CLI!
```
