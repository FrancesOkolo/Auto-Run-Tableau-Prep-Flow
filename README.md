Certainly, here's the instruction in a more markdown-friendly format:

# Setting Up a Python Script to Run Monthly with Task Scheduler

## Step 1: Open Task Scheduler

You can search for Task Scheduler in the Start Menu.

## Step 2: Create Basic Task

Click on "Create Basic Task".

## Step 3: Name Your Task

Name your task and add a description if you want.

## Step 4: Set the Trigger

On the "Trigger" screen, select "Monthly".

## Step 5: Select the Day and Month

Select the day and month you want the task to run.

## Step 6: Choose the Action

On the "Action" screen, select "Start a program".

## Step 7: Enter the Path to Python Executable

In "Program/script", input the path to your Python executable. It is usually:

```
C:\Users\<Username>\AppData\Local\Programs\Python\Python39\python.exe
```

Replace `<Username>` with your username and adjust Python version as necessary.

## Step 8: Add Path to Your Python Script

In "Add arguments", input the path to your script: 

```
C:\path\to\your\script.py
```

Replace this with the actual path to your script.

## Step 9: Finish Creating Task

Click "Next" and then "Finish" to create the task.

Your Python script is now set to run once a month. Remember to manually update your `networth.xls` file before the script runs each month. If your file is not updated before the script runs, the script will use the old data from the previous month. 

In this setup, you don't need the `watchdog` library or any of the file monitoring code. The script will just be executed by Task Scheduler at the scheduled time.
