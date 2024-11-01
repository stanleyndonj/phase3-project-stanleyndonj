

# Phase 3 CLI+ORM Project: Football Management System

A command-line interface football management system. This system will grant the user the rights to manage a simple database of football leagues, teams, and players. It will allow creating, viewing, updating, and deleting records for each of these entities, leveraging an SQLAlchemy ORM to manage database interactions.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Database Models](#database-models)
- [CLI Commands](#cli-commands)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This small project will demonstrate the use of SQLAlchemy ORM, handling relational database interactions from a Python CLI application. It will enable users to manage a database of football leagues, teams, and players, having relationships defined between these entities. The following is part of a Phase 3 project for a CLI+ORM assignment, where the main objectives were:

1. Implementing a CLI that solves a real-world problem.
2. Using SQLAlchemy to create and manage a relational database with 3+ related tables.
3. Structuring the project, environment configuration and documentation should follow the best practices.

## Features

- **CRUD Operations**: Create, read, update, and delete entries for leagues, teams, and players.
- **Relational Database**: One-to-many relationships between League -> Teams and Team -> Players.
- **Validation and Feedback**: The CLI provides input validation and user feedback for successful operations.
- **Modular Design**: Organized into separate modules for CLI, models, and database setup.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:stanleyndonj/phase3-project-stanleyndonj.git
cd phase3-project-stanleydonjr
```

### 2. Set up the Virtual Environment with Pipenv

Make sure you have **Pipenv** installed. If not, install it with:

```bash
pip install pipenv
```

Then, install the project dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

### 3. Initialize the Database

Run the following command to initialize the database and create the required tables:

```bash
python reset_db.py
```

This script will create a new SQLite database (`football.db`) in the project directory and set up the tables for leagues, teams, and players.

## Dependencies

The project dependencies are listed in the `Pipfile`. Key dependencies include:

- **SQLAlchemy**: For ORM and database management.
- **ipdb**: For debugging.
- **Faker**: For generating mock data (if used).
- **pytest**: For testing.

## Project Structure

```
phase3-project-stanleydonjr/
├── .github/            
├── lib/
│   ├── __pycache__/      
│   ├── cli.py            
│   ├── football.db       
│   ├── models.py         
│   └── reset_db.py       
├── .canvas               
├── .gitignore            
├── LICENSE.md            
├── Pipfile               
├── Pipfile.lock          
└── README.md             
```

- **`lib/cli.py`**: Contains the CLI commands for interacting with the database.
- **`lib/models.py`**: Defines the SQLAlchemy ORM models for `League`, `Team`, and `Player`.
- **`lib/reset_db.py`**: Script to reset and initialize the SQLite database.
- **`football.db`**: The SQLite database file, created when running `reset_db.py`.

## Usage

To start the CLI application, run:

```bash
python lib/cli.py
```

This will open the main menu, where you can navigate through the options to manage leagues, teams, and players.

## Database Models

1. **League**
   - Attributes: `id`, `name`
   - Relationships: One-to-many with `Team`
   
2. **Team**
   - Attributes: `id`, `name`, `league_id`
   - Relationships: Many-to-one with `League`, one-to-many with `Player`

3. **Player**
   - Attributes: `id`, `name`, `team_id`
   - Relationships: Many-to-one with `Team`

Each model includes methods for creating, updating, and deleting records, as well as methods for displaying information.

## CLI Commands

The CLI supports the following operations:

- **League Management**
  - Create a new league.
  - View all leagues.
  - Delete a league.

- **Team Management**
  - Create a new team within a league.
  - View all teams within a league.
  - Delete a team.

- **Player Management**
  - Add a player to a team.
  - View all players within a team.
  - Remove a player from a team.

The CLI provides prompts for each action, with validation to ensure that IDs and names are entered correctly. Additionally, feedback messages are provided to confirm each successful operation.

## Testing

Testing is implemented with **pytest**. To run the tests, ensure you are in the project directory with the Pipenv environment active and run:

```bash
pytest
```

This will execute any tests defined within the project, ensuring that functionality is working as expected.

## Contributing

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes and commit them.
4. Push to your branch and open a pull request.

Please ensure that your code adheres to the project’s coding standards and includes appropriate tests.

## License

This project is licensed under the terms of the MIT License. See `LICENSE.md` for more details.

---