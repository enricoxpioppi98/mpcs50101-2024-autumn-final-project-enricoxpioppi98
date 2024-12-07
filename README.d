Below is the finalized README with improved formatting and code blocks. You can copy and paste this directly into a .md file:

# Task Manager CLI

A simple command-line tool for creating, listing, querying, and managing tasks. Tasks are stored on your local machine in a pickle file (`~/.todo.pickle`) and can be manipulated through various command-line options.

## Features

- **Add Tasks:** Add new tasks with optional due dates and custom priority levels.
- **List Tasks:** Display all incomplete tasks, sorted by due date and priority.
- **Mark Tasks as Done:** Mark a task as completed by its unique ID.
- **Delete Tasks:** Remove tasks by their unique ID.
- **Query Tasks:** Search for incomplete tasks containing given search terms.
- **Generate Reports:** Produce a detailed report of all tasks (completed and incomplete).

## File Structure

- **`todo.py`**: Main CLI entry point. Handles command-line arguments and calls methods on the `Tasks` object.
- **`tasks.py`**: Contains the `Tasks` class, which manages a collection of `Task` objects. This includes functionality to load, save, add, list, delete, mark done, generate reports, and query tasks.
- **`task.py`**: Defines the `Task` class, representing individual tasks with attributes such as name, priority, created date, completed date, and due date.

## Usage

Run the `todo.py` script with various command-line arguments to manage your tasks:

```bash
python todo.py [options]

Adding a Task

python todo.py --add "Buy groceries"

You can optionally include a due date and priority:

python todo.py --add "Buy groceries" --due 12/25/2024 --priority 3

	•	--due should be in MM/DD/YYYY format.
	•	--priority should be an integer (1, 2, or 3). The default priority is 1.

Listing Incomplete Tasks

python todo.py --list

This displays all incomplete tasks, sorted by due date and then by priority.

Marking a Task as Completed

python todo.py --done <TASK_ID>

Replace <TASK_ID> with the unique ID of the task you want to mark as completed. The unique ID is shown in the list or report.

Deleting a Task

python todo.py --delete <TASK_ID>

Replace <TASK_ID> with the unique ID of the task you want to delete.

Querying Tasks

python todo.py --query "search terms"

This searches all incomplete tasks for the given terms (case-insensitive).

Generating a Report

python todo.py --report

This generates a comprehensive report of all tasks, including those completed.

Task Storage

Tasks are saved as a pickle file in your home directory under the filename .todo.pickle. This ensures persistence across sessions. If you want to start fresh, you can delete this file, but note that you’ll lose all your saved tasks.

