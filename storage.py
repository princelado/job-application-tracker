import csv
import json
from pathlib import Path


DEFAULT_JSON_FILE = "applications.json"


def load_applications(filename: str = DEFAULT_JSON_FILE) -> list[dict]:
    file_path = Path(filename)

    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []
    except (json.JSONDecodeError, OSError):
        return []


def save_applications(applications: list[dict], filename: str = DEFAULT_JSON_FILE) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(applications, file, indent=4)


def export_to_csv(applications: list[dict], filename: str = "applications.csv") -> bool:
    if not applications:
        return False

    fieldnames = ["id", "company", "role", "date_applied", "status", "location", "notes"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(applications)

    return True