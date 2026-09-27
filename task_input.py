import priority

def get_task():
    while True:
        try:
            num = int(input("How many tasks do you have? "))

            if num <= 0:
                print("    Please enter a whole number.")
            else:
                break
            
        except ValueError:
            print("    Please enter a whole number.")

    tasks = []

    for i in range(num):

        name = input(f"\n{i+1:02d}. Task name: ")

        while True:

            try:
                days_left = round((float(input("    Days left: "))), 2)

                if days_left <= 0:
                    print("\tDays left must be positive.")
                else:
                    break

            except ValueError:
                print("\tPlease enter a positive number.")

        while True:

            try:
                hours = round((float(input("    Estimated hours required: "))), 2)

                if hours <= 0:
                    print("\tRequired hours must be positive.")
                else:
                    break

            except ValueError:
                print("\tPlease enter a positive number.")

        while True:
            try:
                difficulty = round((float(input("    Level of difficulty (/5): "))), 2)

                if (difficulty > 5) or (difficulty <= 0):
                    print("\tLevel of difficulty must belong to (0,5].")
                else:
                    break
                
            except ValueError:
                print("\tPlease enter a positive number.")

        while True:
            try:
                importance = round((float(input("    Level of importance (/5): "))), 2)

                if (importance > 5) or (importance <= 0):
                    print("\tLevel of importance must belong to (0,5].")
                else:
                    break
                
            except ValueError:
                print("\tPlease enter a positive number.")
        

        task = {
                "name": name,
                "days_left": days_left,
                "hours": hours,
                "difficulty": difficulty,
                "importance": importance
               }

        task["priority_score"] = priority.calculate_priority_score(task)
        task["priority_level"], task["priority_level_num"] = priority.set_priority_level(task)
        
        tasks.append(task)



    return tasks