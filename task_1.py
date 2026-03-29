from pathlib import Path


def total_salary(path: str) -> tuple:
    """
    Read employee salary data from a file and return total and average salary.

    Use raw string or escaping to avoid unicode escape warning in literal
    Expected format per line: "<name>,<salary>"
    Lines with invalid format or non-numeric salary are skipped, but program continues.
    If file is missing, returns (0, 0) and reports missing file.
    """
    total = 0
    good_entries = 0
    path_to_file = Path(path)

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()]  # Trim whitespace and remove empty lines
    except FileNotFoundError:
        print("File not found")
        return (0, 0)

    for line in lines:
        employee_info = line.split(",")
        if len(employee_info) != 2 or not employee_info[1].strip().isdigit():  # Notify about malformed line, skip calculation
            print(f"Invalid line, skipping: {line}")
            continue
        else:
            total += int(employee_info[1].strip())  # adding employee salary to total salaries
            good_entries += 1

    if good_entries == 0:  # Avoid division by zero if no valid rows
        print("No valid salary entries found.")
        return (0, 0)

    average = total / good_entries
    if average % 1 == 0:
        average = int(average)
    return (total, average)
