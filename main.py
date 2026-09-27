import task_input
import display
import priority
import workload
import allocation

#0 WELCOME / INSTRUCTIONS

print("╔======================================╗")
print("║           TASK PRIORITIZER           ║")
print("╚======================================╝\n\n\n\n")


print("Plan your work based on:")
print("   • Task urgency")
print("   • Task difficulty")
print("   • Task importance")
print("   • Estimated time required to complete the task")
print("   • Available daily time\n")

print("Let's get started!\n\n\n")


#1 TASK INPUT

tasks = task_input.get_task()
name_width, days_left_width, hours_width = display.width(tasks)

print("\n\n")

display.display_tasks(tasks, name_width, days_left_width, hours_width)


#2 PRIORITY ANALYSIS

tasks = priority.sort_tasks(tasks)

print("\n\n\n")

display.display_priority(tasks)


#3 MOST URGENT

print("\n\n\n")

display.display_most_urgent(tasks)

#4 WORKLOAD ANALYSIS

print("\n\n\n")

daily_work, total_hours = workload.calculate_workload(tasks)

print("\n")

required_daily_width = display.width_of_required_daily(tasks)
display.display_workload(tasks, total_hours, daily_work, name_width, required_daily_width)

print("\n")
total_required_daily, status = display.comment_workload(tasks, daily_work)


#5 TIME ALLOCATION

print("\n\n\n")
today = display.display_allocation(tasks)

#6 WARNINGS / RECOMMENDATIONS

print("\n\n\n")
display.display_warning(tasks, today, total_required_daily, daily_work)


#7 SUMMARY

print("\n\n")
display.display_summary(tasks, total_hours, daily_work, total_required_daily, status)

print("\n\n\n")

print("╔======================================╗")
print("║           END OF ANALYSIS            ║")
print("╚======================================╝\n\n\n")