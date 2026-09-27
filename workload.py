def calculate_workload(tasks):

    print("══════════════════════════ WORKLOAD ANALYSIS ══════════════════════════\n\n")

    while True:

        try:
            daily_work = round((float(input("How many hours are you willing to work daily? "))), 2)

            if (daily_work < 0) or (daily_work > 24):
                print("    Please enter a number in the range [0,24].")

            else:
                break

        except ValueError:
            print("    Please enter a positive number.")

    total_hours = sum(task["hours"] for task in tasks)

    for task in tasks:
        task["required_daily"] = round(task["hours"] / task["days_left"], 2)

    return daily_work, total_hours