# Task Prioritizer

## Overview

Task Prioritizer is a Python-based command-line project that helps users organize their tasks according to urgency, difficulty, importance, estimated workload, and available daily time.

The program takes task information as input, calculates a priority score for each task, analyzes the total workload, creates a time allocation plan for the current day, and provides warnings and recommendations.

## Features

- Add multiple tasks through the command line.
- Validate task inputs.
- Calculate a priority score for every task.
- Classify tasks into:
  - CRITICAL
  - HIGH
  - MEDIUM
  - LOW
- Sort tasks according to their priority score.
- Identify the most urgent task.
- Calculate the total workload.
- Calculate the daily time required for each task.
- Compare required daily workload with available daily working time.
- Identify urgent tasks.
- Generate a daily time-allocation plan.
- Allocate available time using task priority and estimated hours.
- Display warnings and recommendations.
- Display a final summary of the task analysis.

## Priority Calculation

The priority score is calculated using:

Priority Score = (Difficulty × Estimated Hours × Importance) / Days Left

The score is rounded to two decimal places.

Priority levels are assigned as follows:

| Priority Score | Priority Level |
|---|---|
| 50 or above | CRITICAL |
| 30 to less than 50 | HIGH |
| 10 to less than 30 | MEDIUM |
| Less than 10 | LOW |

## Urgency

A task is considered urgent when:

Days Left ≤ 1.5

Urgent tasks are considered first while creating the daily plan.

## Time Allocation

The program asks the user how many hours are available for the current day.

Urgent tasks are considered first. If the available time is not sufficient to complete a group of tasks, the available time is distributed according to a weight calculated from:

Weight = Priority Score × Estimated Hours

Non-urgent tasks are then considered according to their priority level.

## Input Validation

The program validates user input for:

- Number of tasks
- Days left
- Estimated hours required
- Difficulty level
- Importance level
- Available daily working time
- Available time for today's plan

Invalid numeric input is handled using try-except validation.

Difficulty and importance must be greater than 0 and less than or equal to 5.

Daily working time and today's available time must be between 0 and 24 hours.

## Project Structure

Task_Prioritizer/
│
├── main.py
├── task_input.py
├── priority.py
├── workload.py
├── allocation.py
├── display.py
└── warning.py

### Module Description

**main.py**

Controls the overall execution flow of the program and calls the different modules in sequence.

**task_input.py**

Collects task information from the user and validates the input.

**priority.py**

Calculates priority scores, assigns priority levels, and sorts tasks according to their priority score.

**workload.py**

Calculates the total workload and the amount of work required per day for each task.

**allocation.py**

Creates today's plan by identifying urgent tasks and distributing the available time among tasks.

**display.py**

Displays task information, priority analysis, workload analysis, today's plan, warnings, and the final summary.

**warning.py**

Generates warnings, recommendations, and suggestions based on urgency, priority, workload, and today's allocation.

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

1. Download or clone the repository.
2. Open a terminal in the project directory.
3. Run:

    python main.py

## How to Use

When the program starts, enter the number of tasks you want to analyze.

For each task, enter:

1. Task name
2. Days left
3. Estimated hours required
4. Difficulty level
5. Importance level

The program then performs the analysis and asks for:

- Hours the user is willing to work per day
- Hours available today

Finally, it displays the daily plan, warnings and recommendations, and a summary.

## Example Workflow

Task Input
    ↓
Priority Analysis
    ↓
Most Urgent Task
    ↓
Workload Analysis
    ↓
Today's Time Allocation
    ↓
Warnings / Recommendations
    ↓
Summary

## Project Type

Command-line Python application.

## Author

JAHNVI SWARNKAR