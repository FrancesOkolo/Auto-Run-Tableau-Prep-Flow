# How to Setup a Task in Task Scheduler

1. **Open Task Scheduler:** You can search for it in the Start Menu.

2. **Create a Task:** Click on "Create Basic Task".

3. **Name Your Task:** Give it a meaningful name and add a description if you want.

4. **Set the Trigger:** On the "Trigger" screen, select "Monthly".

5. **Choose the Day and Month:** Select the day and month you want the task to run.

6. **Select the Action:** On the "Action" screen, select "Start a program".

7. **Choose the Program/Script:** In "Program/script", input the path to your Python executable. It is usually `C:\Users\<Username>\AppData\Local\Programs\Python\Python39\python.exe` (replace `<Username>` with your username and adjust Python version as necessary).

8. **Add Arguments:** In "Add arguments", input the path to your script: `C:\path\to\your\script.py` (replace with the actual path to your script).

9. **Finish the Setup:** Click "Next" and then "Finish" to create the task.

---
