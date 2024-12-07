# task.py

import time
from datetime import datetime

class Task:
    """
    Representation of a task.
    
    Attributes:
        created (datetime): The datetime when the task was created.
        completed (datetime): The datetime when the task was completed.
        name (str): The name of the task.
        unique_id (int): Unique identifier for the task.
        priority (int): The priority level of the task (1, 2, or 3). Default is 1.
        due_date (datetime): The optional due date for the task.
    """
    def __init__(self, name, priority=1, due_date=None):
        # Inputs
        self.name = name
        self.priority = priority
        self.due_date = due_date

        # Calculated
        self.created = datetime.now()  # Timestamp of when the task was created (including time)
        self.completed = None  # Initially, completed is None, meaning the task is not finished
        self.unique_id = int(datetime.timestamp(self.created) * 1000)  # Generate a unique ID based on the current timestamp

    def mark_completed(self):
        """Mark the task as completed by setting the completed datetime."""
        self.completed = datetime.now()  # Set completed datetime to the current time

    def __repr__(self):
        """Return a string representation of the task."""
        return f"Task(name={self.name}, priority={self.priority}, created={self.created}, completed={self.completed}, due_date={self.due_date})"




# ------------------------------------------------------------------
# DEBUGGING
# ------------------------------------------------------------------

# washing_the_car = Task("Wash the car", priority=2)

# print("\n")
# print(washing_the_car.created)
# print(washing_the_car.unique_id)
# print("\n")

# washing_the_car.mark_completed()
# print(washing_the_car.completed)