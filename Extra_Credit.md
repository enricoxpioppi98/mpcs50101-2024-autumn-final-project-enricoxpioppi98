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
This is already accounted for in the code submitted.

### 6. Test
On macOS, run
```bash
todo --list
```
to confirm that everything works.
