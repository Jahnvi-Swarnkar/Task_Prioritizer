def calculate_priority_score(task):

    priority_score = round((task["difficulty"] * task["hours"] * task["importance"] / task["days_left"]), 2)
    return priority_score

def set_priority_level(task):

    if task["priority_score"] >= 50:
        priority_level = "CRITICAL"
        priority_level_num = 0
    elif task["priority_score"] >= 30:
        priority_level = "HIGH"
        priority_level_num = 1
    elif task["priority_score"] >= 10:
        priority_level = "MEDIUM"
        priority_level_num = 2
    else:
        priority_level = "LOW"
        priority_level_num = 3

    return priority_level, priority_level_num

def sort_tasks(tasks):

    tasks.sort(key= lambda task: task["priority_score"], reverse=True)
    return tasks