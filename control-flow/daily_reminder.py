# daily_reminder.py

# Prompt the user for task description, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"'{task}' is a medium priority task."
    case "low":
        message = f"'{task}' is a low priority task."
    case _:
        message = "Invalid priority entered."

# Modify the message based on time sensitivity using an if statement
if time_bound == "yes":
    message += " It requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."
else:
    message += " Time sensitivity was not properly indicated."

# Print the final customized reminder
print("Reminder:", message)

