# Task manager application
The application is exactly what the title says, it's a task manager application that you can use to add users with passwords, create task's and assign them to specific users and track the progress of every task and user it also has some additional features unfortunately it doesn't have any **GUI** yet, maybe I'll make one for it in the future but my goal was to focus on the backend of the application. 

## How it works
The application comes with two text files, tasks.txt and users.txt these are used to store all the users and tasks added to the application.
There is already an admin user created and two tasks on the application by default. </br>
</br>
When you first run the application it asks for your username and password and will deny any invalid input if you have registered any other users they will alsobe a valid imput.
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
This option will simply display all the tasks in a neat easy to read format as seen below
> Task:             ######</br>
> Assigned to:      ######</br>
> Date assigned:    ######</br>
> Due date:         ######</br>
> Task complete:    Y/N</br>
> Task description:</br>
> #################



This is one of the biggest python projects I've made so far and I learnt alot from it running into alot of deadends but in the end I made it through.
