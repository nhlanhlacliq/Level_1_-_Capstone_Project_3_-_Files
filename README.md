# Level_1_-_Capstone_Project_3_-_Files

_A task manager program created to keep track of tasks_

The program uses two txt files to store data:
* tasks.txt stores a list of all the tasks being worked on, in the following order:

        - The username of the person to the task is assigned to.
        - The title of the task.
        - A description of the task.
        - The date that the task was assigned.
        - The due date for the task.
        - A ‘Yes’ or ‘No’ value that specifies if the task has been completed or not.

* user.txt stores the username and password for each user that has permission to use the program

_The program works as follows_

The user is able to login (program checks their credentials against the user file),
then they are given the following choices:

      - register a new user (Admin only function. Provide a new user and password, confirm password, then the user is added to the user file).
      - add a new task (provide the user the task will be assigned to - program checks if that user does exist - and the other required details for the task. the task assigned date is defaulted to the current date and completed is defaulted to No).
      - view all tasks (program displays all the current tasks in the task file).
      - view my tasks (program checks the current user and displays only the tasks that have been assigned to them).
      - display statistics (only the admin can see this option. The program diplays the current number of tasks and users in the files).
      - exit (the program exits).
