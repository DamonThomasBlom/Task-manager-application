# Task manager application
The application is exactly what the title says, it's a task manager application that you can use to add users with passwords, create task's and assign them to specific users and track the progress of every task and user it also has some additional features unfortunately it doesn't have any **GUI** yet, maybe I'll make one for it in the future but my goal was to focus on the backend of the application. 

## How it works
The application comes with two text files, tasks.txt and users.txt these are used to store all the users and tasks added to the application.
There is already an admin user created and two tasks on the application by default. </br>
</br>
When you first run the application it asks for your username and password and will deny any invalid input if you have registered any other users they will also be a valid input.
Once you have logged in it will display a main menu to you and will be able to select any option but some features are limited to admin priveleges </br>
## Menu option 
1. Register a user (Admin only)
2. Add a task
3. View all tasks
4. View my tasks
5. Generate reports (Admin only)
6. Display statistics (Admin only)
7. Exit
</br>

### 1.Register a user
Admin is prompted to a new window where they are asked to enter in the new user details and password
if the user already exists an error message will pop up if everything is a valid input a **Successfull** message will be displayed and the user details will be added to the text file "user.txt" 
</br>

### 2.Add a task
User is prompted to a new window that asks for the task details eg. Who is the task assigned to, title of the task, task description etc. The assigned date will be generated automatically and everything will be written to the text file "tasks.txt" in a specific format.
</br>

### 3.View all tasks
This option will simply display all the tasks in a neat easy to read format as seen below.
</br>
 Task: &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;######</br>
 Assigned to:  &ensp;&ensp;&ensp;&ensp;&ensp;    ######</br>
 Date assigned: &ensp;&ensp;&ensp;   ######</br>
 Due date:    &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;     ######</br>
 Task complete:  &ensp;&ensp;&ensp;&ensp;&ensp;  Y/N</br>
 Task description:</br>
 #################
</br>

### 4.View my tasks
This option is very similar to the option above but instead of displaying all the tasks it will only display the task assigned to the user currently signed in.
</br>

### 5.Generate reports
This is quite a complex function which when selected will generate two new text files namely "task_overview.txt" and "user_overview.txt" and will start doing specific calculations which will be written to their respective text file. Each file will contain specific data about the tasks and users currently being tracked with the application 

#### task_overview.txt
This file will contain the following information:
1. Number of tasks that have been generated and tracked using the task_manager.py: 
2. Number of completed tasks:
3. Number of incomplete tasks:
4. Number of tasks that are incomplete and overdue:
5. Percentage of tasks that are incomplete: 
6. Percentage of tasks that are overdue:

#### user-overview.txt
This file will contain the following information: </br>
* Total number of users registered with task_manager.py:
* Total number of tasks that have generated and tracked using task_manager.py:
  </br>
  </br>
For each individual user the following will be displayed about that user:
1. Username:
2. Number of tasks assigned to this user: 
3. Percentage of tasks assigned to this user:
4. Percentage of tasks completed:
5. Percentage of tasks incomplete:
6. Percentage of tasks incomplete and overdue:

> Note: These statistics will not be displayed on screen after running this command but will rather just generate the files and store the information
</br>

### 6.Display statistics
When this is selected then the reports will be generated just like the above function but this time it will display everything to the user.

### 7. Exit
This is pretty simple and straight foward but the program will simply to stop running but all informattion will be saved.
</br>
</br>
>This is one of the biggest python projects I've made so far and I learnt alot from it running into alot of deadends but in the end I made it through.
