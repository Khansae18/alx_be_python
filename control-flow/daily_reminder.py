# daily_reminder.py

# Get user inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match-case for priority description
match priority:
    case "high":
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"
    case _:
        priority_text = "unknown priority"

# Build the reminder message
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority_text} task. Consider completing it when you have free time.")

