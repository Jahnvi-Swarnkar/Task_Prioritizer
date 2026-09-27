import allocation
import warning


# CALCULATE WIDTHS



def width(tasks):

    max_length = max(len(task["name"]) for task in tasks)
    name_width = 30

    if max_length > 30:
        name_width = max_length


    max_length = max(len(str(task["days_left"])) for task in tasks)
    days_left_width = 15

    if max_length > 15:
        days_left_width = max_length


    max_length = max(len(str(task["hours"])) for task in tasks)
    hours_width = 20

    if max_length > 20:
        hours_width = max_length

    return name_width, days_left_width, hours_width



def width_of_required_daily(tasks):

    required_daily_width = max(
    len("Time Required / Day"),
    max(len(str(task["required_daily"])) for task in tasks)
    )

    return required_daily_width




# TASKS


def display_tasks(tasks, name_width, days_left_width, hours_width):

    print("┌" + "─" * 7 + "┬" + "─" * (name_width + 2) + "┬" + "─" * (days_left_width + 2) + "┬" + "─" * (hours_width + 2) + "┐")
    print(f"| {'S.No.':<5} | {'Task Name':<{name_width}} | {'Days Left':<{days_left_width}} | {'Hours Required':<{hours_width}} |")
    print("├" + "─" * 7 + "┼" + "─" * (name_width + 2) + "┼" + "─" * (days_left_width + 2) + "┼" + "─" * (hours_width + 2) + "┤")

    for i, task in enumerate(tasks):
        print(f"| {f'{i+1:02d}.':<5} | {task['name']:<{name_width}} | {task['days_left']:<{days_left_width}} | {task['hours']:<{hours_width}} |")

    print("└" + "─" * 7 + "┴" + "─" * (name_width + 2) + "┴" + "─" * (days_left_width + 2) + "┴" + "─" * (hours_width + 2) + "┘")




# PRIORITY


def display_priority(tasks):

    print("══════════════════════════ PRIORITY ANALYSIS ══════════════════════════\n")

    for i, task in enumerate(tasks):

        print(f"\n{i+1:02d}. {task['name']}:")
        print(f"        Priority Score: {task['priority_score']}")
        print(f"        Priority Level: {task['priority_level']}")




# MOST URGENT


def display_most_urgent(tasks):

    print("══════════════════════════ MOST URGENT TASK ═══════════════════════════\n\n")

    urgent = min(tasks, key= lambda task: task["days_left"])

    print(urgent['name'] + ":\n")
    print(f"  Due in {urgent['days_left']} days.")
    print(f"  Estimated Hours Required: {urgent['hours']}")
    print(f"  Difficulty Level: {urgent['difficulty']}")
    print(f"  Importance Level: {urgent['importance']}\n")
    print(f"Priority: {urgent['priority_level']}")




# WORKLOAD


def display_workload(tasks, total_hours, daily_work, name_width, required_daily_width):

    if total_hours == 1:
        print(f"Total work remaining: {total_hours:10} hour")
    else:
        print(f"Total work remaining: {total_hours:10} hours")

    if daily_work == 1:
        print(f"Available daily time: {daily_work:10} hour\n\n")
    else:
        print(f"Available daily time: {daily_work:10} hours\n\n")


    print("┌" + "─" * 7 + "┬" + "─" * (name_width+2) + "┬" + "─" * (required_daily_width+2) + "┐")
    print(f"| {'S.No.':<5} | {'Task Name':<{name_width}} | {'Time Required / Day':<{required_daily_width}} |")
    print("├" + "─" * 7 + "┼" + "─" * (name_width+2) + "┼" + "─" * (required_daily_width+2) + "┤")

    for i, task in enumerate(tasks):
        print(f"| {f'{i+1:02d}.':<5} | {task['name']:<{name_width}} | {task['required_daily']:<{required_daily_width}} |")

    print("└" + "─" * 7 + "┴" + "─" * (name_width+2) + "┴" + "─" * (required_daily_width+2) + "┘")



def comment_workload(tasks, daily_work):

    total_required_daily = sum(task["required_daily"] for task in tasks)

    required = round(total_required_daily, 2)
    available = round(daily_work, 2)
    shortage = round(total_required_daily - daily_work, 2)
    spare_capacity = round(daily_work - total_required_daily, 2)

    stat_com = []

    if total_required_daily > daily_work:
        status = (f"⚠ Your workload exceeds your available time.")

        if required == 1:
            stat_com1 = (f"Required: {required} hour/day")
        else:
            stat_com1 = (f"Required: {required} hours/day")

        stat_com.append(stat_com1)

        if available == 1:
            stat_com2 = (f"Available: {available} hour/day")
        else:
            stat_com2 = (f"Available: {available} hours/day")

        stat_com.append(stat_com2)

        if shortage == 1:
            stat_com3 = (f"Shortage: {shortage} hour/day")
        else:
            stat_com3 = (f"Shortage: {shortage} hours/day")

        stat_com.append(stat_com3)

    else:
        status = (f"✓ Your workload fits within your available time.")

        if spare_capacity == 1:
            stat_com01 = (f"Spare Capacity: {spare_capacity} hour/day")
        else:
            stat_com01 = (f"Spare Capacity: {spare_capacity} hours/day")

        stat_com.append(stat_com01)

    print(status)

    for com in stat_com:
        print(com)

    return total_required_daily, status




# ALLOCATION


def display_allocation(tasks):

    today, total_time_allocated = allocation.time_allocation(tasks)

    for i, today_task in enumerate(today):

        if today_task["time"] == 1:
            print(f"{i+1:02d}. {today_task['name']}")
            print(f"\tAllocate:     {today_task['time']:.2f} hour\n")

        else:
            print(f"{i+1:02d}. {today_task['name']}")
            print(f"\tAllocate:     {today_task['time']:.2f} hours\n")

    print("───────────────────────────────────────────────────────────────────\n")

    if total_time_allocated == 1:
        print(f"Total time allocated:     {total_time_allocated} hour")
    else:
        print(f"Total time allocated:     {total_time_allocated} hours")

    return today




# WARNING


def display_warning(tasks, today, total_required_daily, daily_work):

    comments = warning.set_war(tasks, today, total_required_daily, daily_work)

    print("══════════════════════ WARNINGS / RECOMMENDATIONS ═════════════════════\n\n")

    for comment in comments:
        if comment[0] == "⚠":
            print(comment, "\n")

    for comment in comments:
        if comment[0] == "→":
            print(comment, "\n")

    for comment in comments:
        if comment[0] == "✓":
            print(comment, "\n")




# SUMMARY


def display_summary(tasks, total_hours, daily_work, total_required_daily, status):

    print("═══════════════════════════════ SUMMARY ═══════════════════════════════\n\n")

    highest_priority = max(tasks, key=lambda task: task["priority_score"])
    most_urgent = min(tasks, key=lambda task: task["days_left"])

    print(f"Number of tasks:              {len(tasks)}")
    print(f"Total workload:               {total_hours:.2f} hours")
    print(f"Available per day:            {daily_work:.2f} hours\n")

    print(f"Highest priority:")
    print(f"    → {highest_priority['name']} ({highest_priority['priority_score']})\n")

    print(f"Most urgent task:")
    if most_urgent['days_left'] == 1:
        print(f"    → {most_urgent['name']} (due in {most_urgent['days_left']} day)\n")
    else:
        print(f"    → {most_urgent['name']} (due in {most_urgent['days_left']} days)\n")

    print(f"Today's recommended workload:")
    print(f"    → {total_required_daily:.2f} hours\n")

    print(f"Status:")
    print(f"    → {status}")