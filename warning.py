def set_war(tasks, today, total_required_daily, daily_work):

    comments = []

    for task in tasks:

        if task["urgency"] == True:

            if task["days_left"] == 1:
                c1 = f"⚠ {task['name']} is due in {task['days_left']} day."
            else:
                c1 = f"⚠ {task['name']} is due in {task['days_left']} days."

            comments.append(c1)

        if task["name"] in [allocation["name"] for allocation in today] and (task["priority_level_num"] <= 1):
            c4 = f"→ {task['name']} should be started today because of its high priority."
            comments.append(c4)

        if (task["name"] not in [allocation["name"] for allocation in today]) and (task["priority_score"] == min(task["priority_score"] for task in tasks)):
            c5 = f"✓ {task['name']} can be postponed."
            comments.append(c5)



    if total_required_daily > daily_work:
    
        if total_required_daily == 1:
            c2 = f"⚠ Your total workload requires {total_required_daily:.2f} hour per day, but you have only {daily_work} available."
        else:
            c2 = f"⚠ Your total workload requires {total_required_daily:.2f} hours per day, but you have only {daily_work} available."
    
        comments.append(c2)

    if today:
        allocation = max(today, key=lambda x: x["time"])
        c3 = f"→ Consider completing the {allocation['name']} first."
        comments.append(c3)

    return comments