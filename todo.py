
import argparse
from datetime import datetime
from tasks import Tasks

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Task manager CLI")

    # Add argument for adding a task
    parser.add_argument('--add', type=str, help='Task name', required=False)
    parser.add_argument('--due', type=str, help='Due date in MM/DD/YYYY format', required=False)
    parser.add_argument('--priority', type=int, help='Priority of the task', default=1, required=False)

    # Add argument for listing tasks
    parser.add_argument('--list', action='store_true', help='List all tasks')

    # Add argument for deleting a task
    parser.add_argument('--delete', type=int, help='Delete a task by ID')

    # Add argument for generating a report of all tasks
    parser.add_argument('--report', action='store_true', help='Generate a report of all tasks')

    # Add argument for querying tasks by search terms
    parser.add_argument('--query', type=str, help='Query tasks based on search terms')

    # Add argument for marking a task as done
    parser.add_argument('--done', type=int, help='Mark a task as completed by ID')

    return parser.parse_args()

def main():
    args = parse_args()
    
    # Instantiate the Tasks object
    tasks = Tasks()

    # If '--add' is provided, call the add method with the given arguments
    if args.add:
        due_date = None
        if args.due:
            # Convert the due date to a datetime object
            try:
                due_date = datetime.strptime(args.due, '%m/%d/%Y')
            except ValueError:
                print("Invalid date format. Please use MM/DD/YYYY.")
                return
        
        tasks.add(args.add, priority=args.priority, due_date=due_date)
    
    # If '--list' is provided, call the list method
    if args.list:
        tasks.list()

    # If '--delete' is provided, call the delete method with the task ID
    if args.delete:
        tasks.delete(args.delete)

    # If '--report' is provided, call the report method
    if args.report:
        tasks.report()

    # If '--query' is provided, call the query method with search terms
    if args.query:
        tasks.query(args.query)

    # If '--done' is provided, mark the task as completed by its ID
    if args.done:
        tasks.done(args.done)

if __name__ == '__main__':
    main()