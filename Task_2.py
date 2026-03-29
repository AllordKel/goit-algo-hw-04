from pathlib import Path


def get_cats_info(path: str) -> list:
    """Reads cat records from a text file and return structured data.

    Expected input format per line: <id>,<name>,<age>.
    <age> should contain only digits.
    In case of malformed line in text file - prints malformed line and skips it from further calculations.

    Returns list of dictionaries. Each dictionary holds info for specific cat with keys: "id", "name", "age".
    Returns None if the file is not found.
    """

    file_path = Path(path)
    resulting_cats_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:  # Open file with explicit UTF-8 encoding for portability.
            lines = [el.strip() for el in file.readlines() if el.strip()]  # Strip leading/trailing whitespace from each line.
    except FileNotFoundError:
        print("File not found")  # Provide a clear error message and return None on missing file.
        return None

    for line in lines:
        cat_info = line.split(",")
        if len(cat_info) != 3 or not cat_info[2].strip().isdigit():  # Notify about malformed line, skip calculation.
            print(f"Invalid line, skipping: {line}")
            continue
        resulting_cats_list.append({"id": cat_info[0].strip(), "name": cat_info[1].strip(), "age": cat_info[2].strip()})

    return resulting_cats_list
