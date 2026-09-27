# Task Prioritizer - Project Statement

## Problem Statement

Students often have multiple academic tasks with different deadlines, difficulty levels, importance, and time requirements. Without a systematic way to compare these factors, it can be difficult to decide which task should be worked on first and how much time should be allocated to each task.

Task Prioritizer is designed to solve this problem by analyzing task urgency, difficulty, importance, estimated workload, and available working time. It calculates a priority score for each task, analyzes the overall workload, and generates a daily time-allocation plan.

## Scope

The project focuses on helping users prioritize and plan academic tasks through a command-line Python application.

The system includes:

- Task input and validation
- Priority score calculation
- Priority-level classification
- Identification of urgent tasks
- Workload analysis
- Daily workload calculation
- Time allocation for the current day
- Warnings and recommendations
- Summary of the overall task situation

The project does not include a graphical user interface, database, user accounts, or cloud-based storage.

## Target Users

The primary target users are students who need to manage multiple academic tasks, assignments, examinations, or other study-related work within limited available time.

## High-Level Features

1. **Task Input**
   - Accepts task details from the user.
   - Validates the entered values.

2. **Priority Analysis**
   - Calculates a priority score using difficulty, estimated hours, importance, and days remaining.
   - Assigns a priority level to each task.
   - Sorts tasks based on priority.

3. **Urgency Analysis**
   - Identifies tasks that are close to their deadlines.
   - Displays the most urgent task.

4. **Workload Analysis**
   - Calculates total remaining workload.
   - Calculates the daily time required for each task.
   - Compares required daily time with the user's available daily time.

5. **Daily Time Allocation**
   - Creates a plan for the current day.
   - Considers urgent tasks first.
   - Allocates available time according to task priority and estimated workload.

6. **Warnings and Recommendations**
   - Displays warnings for urgent tasks and excessive workload.
   - Provides recommendations about which tasks should be started or postponed.

7. **Summary**
   - Displays the number of tasks, total workload, available daily time, highest-priority task, most urgent task, recommended workload, and overall workload status.