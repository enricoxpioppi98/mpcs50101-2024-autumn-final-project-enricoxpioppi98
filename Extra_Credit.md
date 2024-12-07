# Make your task manager program an executable program. This will allow it to be run from any location on your computer.

### 1. Move Task and Tasks classes into todo.py
### 2. Add a Shebang Line
At the very top of the todo.py file, add a shebang line so that your system knows to interpret the file with Python. For a standard Python 3 environment, this often looks like:
```python
#!/usr/bin/env python3
```
### 3. Make the File Executable
On Unix-like systems
```bash
chmod +x todo.py
```
### 4. Place the Script in Your $PATH
To run the script from anywhere without typing the full path, place it in a directory that’s in your $PATH, such as /usr/local/bin for macOS.
```bash
sudo cp todo.py /usr/local/bin/todo
```
### 5. Changing the Data Storage Location
The application currently stores its pickle file in the project directory. To ensure the data file can be accessed from anywhere, store it as a hidden file in the user’s home directory.
To do so, update the Tasks class as follows:
```python
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
```
### 6. Test
On macOS, run
```bash
todo --list
```
to confirm that everything works.
