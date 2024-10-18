import csv

# Function to export tasks from the database to CSV
def export_tasks_to_csv(tasks, filename='tasks.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'data', 'date', 'user_id'])  # CSV header
        for task in tasks:
            writer.writerow([task.id, task.data, task.date, task.user_id])

# Function to read tasks from CSV
def read_tasks_from_csv(filename='tasks.csv'):
    tasks = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks

# Function to write a new task to CSV
def write_task_to_csv(task_data, user_id, filename='tasks.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        task_id = get_new_task_id(filename)  # Generate a new ID for the task
        writer.writerow([task_id, task_data, '2024-09-23', user_id])

# Function to get a new task ID based on the existing tasks in the CSV
def get_new_task_id(filename='tasks.csv'):
    tasks = read_tasks_from_csv(filename)
    return max(int(task['id']) for task in tasks) + 1 if tasks else 1
