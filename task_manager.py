#Capstone Project II
#imports
from datetime import date


today = date.today().strftime("%d %b %Y") #Getting and saving today's date, then formatting it as 'dd mon yyy'
current_user = ''                         #Creating empty variable to keep track of user for later usage

#Login
print("Login")
print("=============")

"""login function - Takes the user's username and checks if that name is in the user.txt file, 
if so (and the password is correct) the program proceeds to the next menu
If the user does not exist or the password is incorrect the program asks the user to input their credentials again, until they are correct.
The user is not made aware of which of their credentials is incorrect as it is a security concern, however, that can be added if needed.
"""
def try_login():
    username = input("Enter username:\n> ")
    password = input("Enter password:\n> ")
    loggedin = False
    with open("user.txt", "r") as userfile:         #Reads the file
        for line in userfile:
            user = line.split()[0].strip(",")       #loops through the file
            user_password = line.split()[1]
            if username == user:
                if password == user_password:
                    loggedin = True
                #print("Password incorrect.")      #uncomment this line to know if the password is incorrect.
    if loggedin:
        print("Log in successful.\n")
        global current_user                     #making the current user a global variable so it is not updated within the login function only
        current_user = username
        open_menu()
    else:
        print("Username/Password incorrect. Please try again.\n")
        try_login()                             #Should the credential be incorrect, the user is asked to try again
        
"""open menu function - only visible once user has logged in. Presents user with menu options 
and opens the necessary funtions depending on user input.
If the current user is the admin he has one more menu option.
"""
def open_menu():
    print("Please select one of the following options:\n===========================================")
    if current_user == 'admin':
        menu_option = input("'r' - register user\n'a' - add task\n'va' - view all tasks\n'vm' - view my tasks\n's' - statistics\n'e' - exit\n> ")
    else:
        menu_option = input("'r' - register user\n'a' - add task\n'va' - view all tasks\n'vm' - view my tasks\n'e' - exit\n> ")
    if menu_option == 'r':
        register_user()
    elif menu_option == 'a':
        add_task()
    elif menu_option == "va":
        view_all_tasks()
    elif menu_option == "vm":
        view_my_tasks()
    elif menu_option == "s":
        if current_user == "admin":
            view_statistics()
        else:                   #if the non admin users select 's' as an option, which isn't available to them. the program takes the back to the menu
            print("Nothing to see here.")
            goto_menu()
    elif menu_option == "e":
        print("Goodbye")
        quit()
    else:               #If the user enter an invalid command. the program prompts them to try again. 
        print("Your input is unrecognized. Please try again.")
        goto_menu()

#register user function, creates a new user (if the user is the admin) and writes the user to the user.txt file
def register_user():
    if current_user == 'admin':
        new_username = input("Enter new username:\n> ")
        new_password = input("Enter new password:\n> ")
        confirm_new_password = input("Please confirm new password: \n> ")

        if new_password == confirm_new_password:
            with open("user.txt", "a") as userfile:
                userfile.write(f"\n{new_username}, {new_password}")
            print(f"{new_username} registered successfully.")
            goto_menu()

        elif new_username != confirm_new_password:      #If passwords do not match the user is asked to try again
            print("Passwords do not match. Please retry.")
            register_user()
    else:                   #If user is not an admin
        print("Only the admin is permitted to register new users.")
        goto_menu()

"""Add task function, the program checks if the user(who the task will be added under) exists first and if not, it prompts the user to try again,
if the user does exist, then the program gets the required details for the task and proceeds to write them into the task.txt file
"""
def add_task():
    task_user = input("Enter username of the person the task is to be assigned to:\n> ")
    user_exists = False
    with open("user.txt", "r") as userfile:
        for line in userfile:
            user = line.split()[0].strip(",")
            if task_user == user:
                user_exists = True
            
    if user_exists:
        print(f"Adding task for {task_user}:")
        task_title = input("Enter the title of the task:\n> ")
        task_description = input("Enter the description of the task:\n> ")
        task_duedate = input("Enter the due date(e.g. 07 Mar 2020) for the task:\n> ")
        task_dateassigned = today
        task_complete = "No"    
        with open("tasks.txt", "a") as taskfile:
            taskfile.write(f"\n{task_user}, {task_title}, {task_description}, {task_dateassigned}, {task_duedate}, {task_complete}")
            print("Task added successfully.\n")
        goto_menu()

    else:
        print(f"{task_user} does not exist. Try again")
        add_task()

#view all tasks function - gets and displays all the tasks currently in the task.txt file
def view_all_tasks():
    print(f"Showing all tasks\n========================")
    with open("tasks.txt", "r") as taskfile:            #Reads the file
        for line in taskfile:
            task_user = line.split(",")[0]              #Splits the different string parts into variables
            task_title = line.split(",")[1]         
            task_description = line.split(",")[2]
            task_dateassigned = line.split(",")[3]
            task_duedate = line.split(",")[4]
            task_complete = line.split(",")[5]
            #Printing and organizing the pasrt into a user friendly format 
            print(f"User\t\t:{task_user}\nTitle\t\t:{task_title}\nDescription\t:{task_description}\nDate assigned\t:{task_dateassigned}\nDate due\t:{task_duedate}\nComplete\t:{task_complete}")
    goto_menu()
            
#view my tasks function checks the current user and displays their relevant tasks from task.txt. 
def view_my_tasks():
    print(f"Showing tasks for {current_user}\n========================")
    with open("tasks.txt", "r") as taskfile:
        for line in taskfile:
            task_user = line.split(",")[0]
            if task_user == current_user:
                task_title = line.split(",")[1]
                task_description = line.split(",")[2]
                task_dateassigned = line.split(",")[3]
                task_duedate = line.split(",")[4]
                task_complete = line.split(",")[5]
                print(f"Title\t\t:{task_title}\nDescription\t:{task_description}\nDate assigned\t:{task_dateassigned}\nDate due\t:{task_duedate}\nComplete\t:{task_complete}")
    goto_menu()

#view statistics function, counts how many users and tasks are present in the relevant files and displays the information 
def view_statistics():
    print("Statistics\n==============")
    count_users = 0
    count_tasks = 0
    with open("user.txt", "r") as userfile:
        for line in userfile:
            count_users += 1
    with open("tasks.txt", "r") as taskfile:
        for line in taskfile:
            count_tasks += 1
    print(f"Number of users\t: {count_users}\nNumber of tasks\t: {count_tasks}")
    goto_menu()

#go to menu function created to allow the user to go back to the main menu when they are ready to, using an empty input to confirm
def goto_menu():
    input("\n(Press Enter to go back.)")
    open_menu()

#After defining functions, program can now run, calling the login function to begin.
try_login()

