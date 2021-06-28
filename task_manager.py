from datetime import date, datetime


# Functions
def reg_user(new_user, new_password, confirm_password):
    global register  # We call the global function here because we will need to change this variable outside our function
    user_file = open("user.txt", 'r')  # Open user.txt in read and write mode to check user and to add on to the list

    list_of_users = []  # We take the text file and split the lines and store all the users in a list
    for line in user_file:
        line = line.split(', ')
        user = line[0]
        list_of_users.append(user)
    # We create a variable that will store whether the username exists or not we will save it as a boolean automatically set to true
    user_does_not_exist = True
    for user in list_of_users:  # Iterate over the list of users and if the new username matches with any of the existing user names we change our boolean variable to false
        if user == new_user:
            user_does_not_exist = False
    user_file.close()
    user_file = open('user.txt', 'a', newline='')
    # Now we check if the new username and password meets all the criteria and if so write it into the user text file
    if new_password == confirm_password and user_does_not_exist == True:  # If the confirm password matches the info will be stored in the user.txt file
        user_file.write(f"\n{new_user}, {new_password}")
        print("Successfully registered new user")
        register = True  # Change our global variable to true so the loop can end
    # If the username already exists we display this error message
    elif user_does_not_exist == False:
        return print("Sorry this username already exists, Please try again")
    # If the new password does not match with the confirm password we display this error message
    elif new_password != confirm_password:
        print("Sorry the confirmed password doesn't match")

    user_file.close()


def add_task(task_username, task_title, task_description, assign_date, due_date, completed):
    task_file = open("tasks.txt", "a", newline='')  # Open tasks.txt in append mode to add onto the list
    task_file.write(f"\n{task_username}, {task_title}, {task_description}, {assign_date}, {due_date}, {completed}")
    print("You successfully added a task")
    task_file.close()


def view_all():
    task_file = open("Tasks.txt", "r")
    for line in task_file:
        line = line.rstrip()
        line = line.split(", ")  # Split each line into these variables and display it in an easy to read format
        print(f'''_____________________________________________________
Task:                   {line[1]}
Assigned to:            {line[0]}
Date assigned:          {line[3]}
Due date:               {line[4]}
Task Complete?          {line[5]}
Task description:
{line[2]}
''')
    task_file.close()


def view_mine():
    with open("tasks.txt", 'r') as task_file:
        list_of_lines = task_file.readlines()
        number_of_items_in_line = len(list_of_lines[0].split(', '))
        new_text = []
        task_number = 1
        if number_of_items_in_line == 6:  # If the line does not contain a task number we run this code
            for i in list_of_lines:
                i = i.replace('\n', '')
                i = i + f", {task_number}\n"
                task_number += 1
                new_text.append(i)
    if new_text != []:
        with open("tasks.txt", 'w') as task_file:
            task_file.writelines(new_text)
    # We only print the line out if the user name matches with the logged in user
    task_file = open("tasks.txt", 'r')
    for line in task_file:
        line = line.rstrip()
        line = line.split(", ")

        if user_login == line[0]:  # Only if the logged in username matches with the task who's user it is assigned to will be print out(if the task does not match with the users name then it will not be printed out
            print(f'''_____________________________________________________
Task Number:            {line[6]}
Task:                   {line[1]}
Assigned to:            {line[0]}
Date assigned:          {line[3]}
Due date:               {line[4]}
Task Complete?          {line[5]}
Task description:
{line[2]}
    ''')
    task_file.close()


def main_menu():
    if user_login != 'admin':  # If the user is not logged in as an admin this menu will display
        print('''\n######### Main Menu ##########
r - register user
a - add task
va - view all tasks
vm- view my tasks
e - exit''')
        option = input("Option: ")
        return option
    elif user_login == 'admin':  # If the user is logged in as an admin they will get this unique menu
        print('''######### Main Menu ##########
r - register user
a - add task
va - view all tasks
vm- view my tasks
gr - generate reports
ds - display statistics
e - exit''')
        option = input("Option: ")  # Store their option into a variable
        return option
# We call this function when ever we want to display the menu again


def generate_reports():
    user_file = open('user.txt', 'r')
    task_file = open('tasks.txt', 'r')
    num_of_tasks = 0  # Total number of tasks that have been generated and tracked using the task_manager.py.
    num_of_incompleted_tasks = 0  # Total number of uncompleted tasks.
    num_of_completed_tasks = 0  # Total number of completed tasks.
    task_overdue = 0  # Total number of tasks that haven’t been completed and that are overdue

    for line in task_file:
        line = line.rstrip()
        line = line.split(", ")
        if line[
            1] != '':  # If the second index in the line is not blank we know there is a task title there so we add to the total number of tasks
            num_of_tasks += 1
        if line[5] == 'Yes':  # This index checks if the task is completed
            num_of_completed_tasks += 1
        if line[5] == 'No':
            num_of_incompleted_tasks += 1
        # To see if a task if over due we need to convert the due date and todays date into data we can compare
        due_date = line[4]
        due_date = datetime.strptime(due_date, "%d %b %Y")
        now = datetime.now()
        if due_date < now and line[5] == 'No':  # If its past the due date and incomplete
            task_overdue += 1
    percentage_incomplete = (num_of_incompleted_tasks / num_of_tasks) * 100  # Percentage of tasks that are incomplete
    percentage_overdue = (task_overdue / num_of_tasks) * 100  # Percentage of tasks that are overdue
    # Open the new file to store the data
    task_overview = open('task_overview.txt', 'w')
    task_overview.write(f'''TASK OVERVIEW
Number of tasks that have been generated and tracked using the task_manager.py:  {num_of_tasks}
Number of completed tasks: {num_of_completed_tasks}
Number of incompleted tasks: {num_of_incompleted_tasks}
Number of tasks that haven’t been completed and that are overdue: {task_overdue}
Percentage of tasks that are incomplete: {percentage_incomplete}%
Percentage of tasks that are overdue: {percentage_overdue}%
''')
    num_of_users = 0
    list_of_users = []  # First make a list containing all the user names
    for line in user_file:
        line = line.rstrip()
        user, password = line.split(", ")
        if line[
            0] != '':  # If the first index in the line is not an empty string we know there is a username there so we add to the count of users
            num_of_users += 1
        list_of_users.append(user)  # Append the name the the list of names
    with open('user_overview.txt', 'w') as user_overview:
        user_overview.write(f'''USER OVERVIEW
Total number of users registered with task_manager.py: {num_of_users}
Total number of tasks that have been generated and tracked using the task_manager.py: {num_of_tasks}

    ''')
    # We iterate over the list of names
    for name in list_of_users:
        task_file = open('tasks.txt', 'r')
        tasks_assigned_to_user = 0
        tasks_completed = 0
        not_complete_overdue = 0
        for line in task_file:
            line = line.rstrip()
            line = line.split(", ")
            if line[0] == name:  # If the name and the person this is assigned to matches
                tasks_assigned_to_user += 1
            if line[0] == name and line[5] == 'Yes':
                tasks_completed += 1
            due_date = line[4]  # We change current date and due date into data we can compare
            due_date = datetime.strptime(due_date, "%d %b %Y")
            now = datetime.now()
            if due_date < now and line[5] == 'No' and name == line[0]:
                not_complete_overdue += 1
        if tasks_assigned_to_user != 0:
            # We have to do these calculations after our for loop because initially some variables will equal 0 and we cannot divide by a zero
            percentage_of_task = (tasks_assigned_to_user / num_of_tasks) * 100
            percentage_completed = (tasks_completed / tasks_assigned_to_user) * 100
            percentage_to_be_completed = 100 - percentage_completed
            percentage_not_complete_overdue = (not_complete_overdue / tasks_assigned_to_user) * 100
            # Write the data into the text file
            user_overview = open('user_overview.txt', 'a')
            user_overview.write(f'''User: {name}
        
Number of tasks assigned to this user: {tasks_assigned_to_user}
Percentage of tasks assigned to this user: {percentage_of_task}%
Percentage of tasks completed: {percentage_completed}%
Percentage of tasks incomplete: {percentage_to_be_completed}%
Percentage of tasks incomplete and overdue: {percentage_not_complete_overdue}%\n
''')
        elif tasks_assigned_to_user == 0:
            # Write the data into the text file
            user_overview = open('user_overview.txt', 'a')
            user_overview.write(f'''User: {name}

Number of tasks assigned to this user: {tasks_assigned_to_user}
Percentage of tasks assigned to this user: 0%
Percentage of tasks completed: 0%
Percentage of tasks incomplete: 0%
Percentage of tasks incomplete and overdue: 0%\n
''')


# format of user.txt
# username, password

# format of tasks.txt
# task_username, task_name, task_description, assign_date, due_date, completed

# This variable will store todays date
today = date.today()

# User Login
login = False
user_login = ''
user_file = open("user.txt", "r+")
while login == False:  # This loop will repeat as long as login equals false
    user_login = input("Enter username: ")
    user_password = input("Enter password: ")
    for line in user_file:
        line = line.rstrip()
        user, password = line.split(", ")  # We split the line into variables we can use
        if user_login == user and user_password == password:  # If the user and password match we set login to True so the user can move on
            login = True
            print("Successfully logged in\n")
            break
        else:
            print("Please enter in a valid username and password.")
    user_file.seek(0)
user_file.close()

# Display menu for logged in user
option = main_menu()
while True:  # We run the whole application in a loop so the menu will constantly pop up until the user exits the program
    # register a user (Admin only
    if option == 'r' and user_login == 'admin':  # Only the admin can register a user
        register = False  # This variable will be changed to True inside our function reg_user to end the loop
        while register == False:
            new_user = input("Please enter in the new users username: ")
            new_password = input("Please enter in the new users password: ")
            confirm_password = input("Enter in password again to confirm it: ")
            reg_user(new_user, new_password, confirm_password)
        option = main_menu()
    elif option == 'r' and user_login != 'admin':  # If the user is not an admin we tell them they do not have permission
        print("Sorry you do not have permission to register a user")
        option = main_menu()

    # Add a task
    if option == 'a':
        print("Enter in the following")
        task_username = input("Username of the person this task is assigned to: ")
        task_title = input("Title of this task: ")
        task_description = input("Task description: ")
        assign_date = today.strftime(
            "%d %b %Y")  # We store all this inputs into seperate variables and then write it into the task file
        due_date = input("Due date(e.g 21 feb 2021): ")
        completed = "No"
        add_task(task_username, task_title, task_description, assign_date, due_date, completed)
        option = main_menu()

    # View all tasks
    if option == "va":
        view_all()
        option = main_menu()

    # View my tasks
    if option == "vm":
        view_mine()
        second_option = input('''\nSelect a task number: ?
exit: -1
option:''')  # Second option will store the task number the user selects
        task_file = open("tasks.txt", 'r')
        list_of_lines = task_file.readlines()  # First read all the lines from the file and store it in a variable so we can change it later
        if second_option != '-1':
            task_choice = int(second_option) - 1  # We subtract 1 because python indexes start at 0
            third_option = input('''\n1- Mark this task as complete
2- Edit this task
Option: ''')  # Third option will store whether the user wants to edit the task or mark as complete
            if third_option == '1':
                items_in_line = list_of_lines[task_choice].split(
                    ', ')  # Split the line the of the task that the user selects
                string = ', '
                items_in_line[5] = 'Yes'  # Change the value of this index to yes to mark the task as complete
                new_line = string.join(items_in_line)
                list_of_lines[task_choice] = new_line
                with open('tasks.txt', 'w') as task_file:
                    task_file.writelines(list_of_lines)  # Write the updated data into the text file in the same format
            if third_option == '2':
                fourth_option = input('''\nWould you like to:
1- Change the user this task is assigned to
2- Change the due date of this task
Option: ''')
                if fourth_option == '1':  # We aply the same knowledge we just used to change the name of the user this task is assigned to
                    new_user_for_task = input('Enter the new user you would like to assign this task to: ')
                    items_in_line = list_of_lines[task_choice].split(', ')
                    string = ', '
                    items_in_line[0] = new_user_for_task
                    new_line = string.join(items_in_line)
                    list_of_lines[task_choice] = new_line
                    with open('tasks.txt', 'w') as task_file:
                        task_file.writelines(list_of_lines)
                if fourth_option == '2':
                    new_due_date = input('Enter the new due date of this task(eg 21 Feb 2021): ')
                    items_in_line = list_of_lines[task_choice].split(', ')
                    string = ', '
                    items_in_line[4] = new_due_date
                    new_line = string.join(items_in_line)
                    list_of_lines[task_choice] = new_line
                    with open('tasks.txt', 'w') as task_file:
                        task_file.writelines(list_of_lines)
        elif second_option == '-1':
            option = main_menu()

    # Display statistics (Admin only)
    if user_login == 'admin' and option == 'ds':
        generate_reports()  # We run our function the generate reports in case the user hasn't done this yet
        user_file = open('user_overview.txt', 'r+')
        task_file = open('task_overview.txt', 'r+')
        user_data = user_file.read()  # We read the data from both files and store it in variables
        task_data = task_file.read()  # We don't need to format it since it is already in a neat format
        print(task_data + user_data)  # So we simply print it as is
        option = main_menu()

    # Generate reports
    if user_login == 'admin' and option == 'gr':
        generate_reports()
        option = main_menu()

    # Exit
    if option == 'e':
        break  # When the user selects to exit we simply break the loop
