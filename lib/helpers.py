from models import session, User, FitnessGoal, Progress

def exit_program():
    print("Goodbye!")
    exit()

def add_new_user():
    name = input("Enter user name: ").strip()
    email = input("Enter user email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.")
        return

    # Check if email is unique
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print(f"User with email {email} already exists.")
        return

    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    print(f"User {name} added successfully.")

def add_fitness_goal():
    email = input("Enter user email: ").strip()
    user = session.query(User).filter_by(email=email).first()

    if not user:
        print(f"No user found with email {email}.")
        return

    goal_name = input("Enter fitness goal name: ").strip()
    description = input("Enter goal description: ").strip()
    target = input("Enter target value (e.g., '5 km', '70 kg'): ").strip()
    target_type = input("Enter target type (e.g., 'distance', 'weight'): ").strip()

    if not goal_name or not target or not target_type:
        print("Goal name, target, and target type cannot be empty.")
        return

    new_goal = FitnessGoal(
        name=goal_name,
        description=description,
        target=target,
        target_type=target_type,
        user_id=user.id
    )
    session.add(new_goal)
    session.commit()
    print(f"Fitness goal '{goal_name}' added successfully for {user.name}.")

def track_progress():
    goal_id = input("Enter goal ID: ").strip()
    goal = session.query(FitnessGoal).filter_by(id=goal_id).first()

    if not goal:
        print(f"No goal found with ID {goal_id}.")
        return

    value = input("Enter progress value (e.g., '2 km', '65 kg'): ").strip()
    notes = input("Enter any notes for this progress update (optional): ").strip()

    if not value:
        print("Progress value cannot be empty.")
        return

    new_progress = Progress(
        goal_id=goal.id,
        value=value,
        notes=notes
    )
    session.add(new_progress)
    session.commit()
    print(f"Progress for goal '{goal.name}' updated successfully.")

def view_fitness_goals():
    email = input("Enter user email: ").strip()
    user = session.query(User).filter_by(email=email).first()

    if not user:
        print(f"No user found with email {email}.")
        return

    goals = session.query(FitnessGoal).filter_by(user_id=user.id).all()
    if not goals:
        print(f"{user.name} has no fitness goals.")
        return

    print(f"\nFitness Goals for {user.name}:")
    for goal in goals:
        print(f"ID: {goal.id}, Goal: {goal.name}, Target: {goal.target}")

def view_goal_progress():
    goal_id = input("Enter goal ID: ").strip()
    goal = session.query(FitnessGoal).filter_by(id=goal_id).first()

    if not goal:
        print(f"No goal found with ID {goal_id}.")
        return

    progress_entries = session.query(Progress).filter_by(goal_id=goal.id).all()

    if not progress_entries:
        print(f"No progress entries for goal '{goal.name}'.")
        return

    print(f"\nProgress for '{goal.name}':")
    for entry in progress_entries:
        print(f"Date: {entry.date}, Value: {entry.value}, Notes: {entry.notes}")

def delete_fitness_goal():
    goal_id = input("Enter goal ID: ").strip()
    goal = session.query(FitnessGoal).filter_by(id=goal_id).first()

    if not goal:
        print(f"No goal found with ID {goal_id}.")
        return

    session.delete(goal)
    session.commit()
    print(f"Fitness goal '{goal.name}' deleted successfully.")
