# tasks.py
from task import Task

import os
import pickle
from datetime import datetime, date

class Tasks:
    def __init__(self, filename=None):
        if filename is None:
            # Set the pickle file to be in the user's home directory
            home_dir = os.path.expanduser("~")  # Get the user's home directory
            filename = os.path.join(home_dir, '.todo.pickle')  # Store it as an invisible file
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a pickled file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
                tasks = data['tasks']
                # Ensure all tasks have 'created' as a datetime object
                for task in tasks:
                    if isinstance(task.created, date) and not isinstance(task.created, datetime):
                        task.created = datetime.combine(task.created, datetime.min.time())
                    if task.completed and isinstance(task.completed, date) and not isinstance(task.completed, datetime):
                        task.completed = datetime.combine(task.completed, datetime.min.time())
                tasks.sort(key=lambda task: task.created)
                return tasks
        else:
            return []

    def pickle_tasks(self):
        """Pickle the task list and last used ID to a file."""
        with open(self.filename, 'wb') as f:
            data = {'tasks': self.tasks}
            pickle.dump(data, f)

    def add(self, name, priority=1, due_date=None):
        """Add a new task to the task list."""
        task = Task(name, priority, due_date)
        self.tasks.append(task)
        self.pickle_tasks()

    def list(self):
        """Display a list of not completed tasks, sorted by due date and priority."""
        # Filter tasks that are not completed
        not_completed_tasks = [task for task in self.tasks if task.completed is None]

        # Sort tasks: First by due date (ascending), then by priority (descending)
        not_completed_tasks.sort(key=lambda task: (
            datetime.combine(task.due_date, datetime.min.time()) if isinstance(task.due_date, date) else 
            (datetime.today() if task.due_date is None else task.due_date),
            -task.priority
        ))

        # Display header
        print("\n")
        print(f"{'ID':<15} {'Age':<5} {'Due Date':<10} {'Priority':<10} {'Task':<20}")
        print("-" * 60)

        # Display each task
        for task in not_completed_tasks:
            age = (datetime.today() - task.created).days
            due_date = task.due_date.strftime('%m/%d/%Y') if task.due_date else "-"
            print(f"{task.unique_id:<15} {f'{age}d':<5} {due_date:<10} {task.priority:<10} {task.name:<20}")
        print("\n")

    def delete(self, task_id):
        """Delete a task by its unique ID."""
        task_to_delete = None

        # Find the task with the given unique_id
        for task in self.tasks:
            if task.unique_id == task_id:
                task_to_delete = task
                break

        if task_to_delete:
            # Remove the task from the list
            self.tasks.remove(task_to_delete)
            # Update the pickle file
            self.pickle_tasks()
            print(f"Task with ID {task_id} has been deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def done(self, task_id):
        """Mark a task as completed by its unique ID."""
        task_to_mark = None

        # Find the task with the given unique_id
        for task in self.tasks:
            if task.unique_id == task_id:
                task_to_mark = task
                break

        if task_to_mark:
            # Mark the task as completed
            task_to_mark.mark_completed()
            # Update the pickle file
            self.pickle_tasks()
            print(f"Task with ID {task_id} has been marked as completed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def report(self):
        """Display a report of all tasks, including both completed and incomplete tasks."""
        # Sort tasks: First by due date (ascending), then by priority (descending)
        self.tasks.sort(key=lambda task: (
            datetime.combine(task.due_date, datetime.min.time()) if isinstance(task.due_date, date) else task.due_date,
            -task.priority  # Sort by priority in descending order
        ))

        # Display header
        print("\n")
        print(f"{'ID':<15} {'Age':<5} {'Due Date':<10} {'Priority':<10} {'Task':<20} {'Created':<25} {'Completed':<25}")
        print("-" * 120)
        print("\n")

        # Display each task
        for task in self.tasks:
            age = (datetime.today() - task.created).days
            due_date = task.due_date.strftime('%m/%d/%Y') if task.due_date else "-"
            created_date = task.created.strftime('%a %b %d %H:%M:%S %Z %Y')
            completed_date = task.completed.strftime('%a %b %d %H:%M:%S %Z %Y') if task.completed else "-"
            
            print(f"{task.unique_id:<15} {f'{age}d':<5} {due_date:<10} {task.priority:<10} {task.name:<20} {created_date:<25} {completed_date:<25}")

    def query(self, search_terms):
        """Search for tasks based on multiple search terms. Only return non-completed tasks."""
        terms = search_terms.lower().split()

        matched_tasks = [
            task for task in self.tasks
            if task.completed is None and any(term in task.name.lower() for term in terms)
        ]

        matched_tasks.sort(key=lambda task: (
            datetime.combine(task.due_date, datetime.min.time()) if isinstance(task.due_date, date) else task.due_date,
            -task.priority
        ))

        # Display header
        print("\n")
        print(f"{'ID':<15} {'Age':<5} {'Due Date':<10} {'Priority':<10} {'Task':<20}")
        print("-" * 60)

        # Display each task
        for task in matched_tasks:
            age = (datetime.today() - task.created).days
            due_date = task.due_date.strftime('%m/%d/%Y') if task.due_date else "-"
            print(f"{task.unique_id:<15} {f'{age}d':<5} {due_date:<10} {task.priority:<10} {task.name:<20}")
        print("\n")


# ------------------------------------------------------------------
# DEBUGGING
# ------------------------------------------------------------------

# tasks = Tasks()
# Add some tasks for testing
# tasks.add('Walk dog', priority=1, due_date=datetime(2023, 4, 17))
# tasks.add('Study for finals', priority=3, due_date=datetime(2023, 3, 20))
# tasks.add('Buy eggs', priority=2)
# tasks.add('Make eggs', priority=1)

# tasks.delete(1733593151830)
# tasks.delete(1733593151830)

# tasks.done(1733593151829)

# tasks.list()
# tasks.report()
# Mark a task as completed
# tasks.done(1733590154630)  # Mark 'Walk dog' as completed (replace with actual ID)

# Perform the query search
# tasks.query('dog')
# print("\n")