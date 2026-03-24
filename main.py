import re
from tracker import JobTracker
from utils import (
    VALID_STATUSES,
    normalise_status,
    print_applications,
    print_statistics,
)


def display_menu() -> None:
    print("\n" + "=" * 40)
    print("JOB APPLICATION TRACKER")
    print("=" * 40)
    print("1. Add application")
    print("2. View applications")
    print("3. Update application status")
    print("4. Search by company")
    print("5. Search by role")
    print("6. Filter by status")
    print("7. Delete application")
    print("8. Show statistics")
    print("9. Export to CSV")
    print("10. Exit")


def get_status_input(prompt: str = "Enter status: ") -> str:
    print(f"Valid statuses: {', '.join(VALID_STATUSES)}")
    user_input = input(prompt)
    return normalise_status(user_input)


def add_application_flow(tracker: JobTracker) -> None:
    print("\nADD APPLICATION")
    company = input("Company: ")
    role = input("Role: ")
    while True:
        try:
            date_applied = input("Date applied (YYYY-MM-DD): ")
            break
        except ValueError:
            continue
    status = get_status_input()
    location = input("Location: ")
    notes = input("Notes: ")

    success, message = tracker.add_application(
        company=company,
        role=role,
        date_applied=date_applied,
        status=status,
        location=location,
        notes=notes,
    )
    print(message)


def view_applications_flow(tracker: JobTracker) -> None:
    applications = tracker.view_applications()
    print_applications(applications)


def update_status_flow(tracker: JobTracker) -> None:
    print("\nUPDATE APPLICATION STATUS")

    try:
        app_id = int(input("Enter application ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    new_status = get_status_input("Enter new status: ")
    success, message = tracker.update_status(app_id, new_status)
    print(message)


def search_by_company_flow(tracker: JobTracker) -> None:
    company_name = input("\nEnter company name to search: ")
    results = tracker.search_by_company(company_name)
    print_applications(results)


def search_by_role_flow(tracker: JobTracker) -> None:
    role_name = input("\nEnter role name to search: ")
    results = tracker.search_by_role(role_name)
    print_applications(results)


def filter_by_status_flow(tracker: JobTracker) -> None:
    status = get_status_input("\nEnter status to filter by: ")
    results = tracker.filter_by_status(status)
    print_applications(results)


def delete_application_flow(tracker: JobTracker) -> None:
    print("\nDELETE APPLICATION")

    try:
        app_id = int(input("Enter application ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    success, message = tracker.delete_application(app_id)
    print(message)


def show_statistics_flow(tracker: JobTracker) -> None:
    stats = tracker.get_statistics()
    print_statistics(stats)


def export_csv_flow(tracker: JobTracker) -> None:
    filename = input("\nEnter CSV filename (or press Enter for applications.csv): ").strip()

    if not filename:
        filename = "applications.csv"

    success, message = tracker.export_applications_to_csv(filename)
    print(message)


def main() -> None:
    tracker = JobTracker()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_application_flow(tracker)
        elif choice == "2":
            view_applications_flow(tracker)
        elif choice == "3":
            update_status_flow(tracker)
        elif choice == "4":
            search_by_company_flow(tracker)
        elif choice == "5":
            search_by_role_flow(tracker)
        elif choice == "6":
            filter_by_status_flow(tracker)
        elif choice == "7":
            delete_application_flow(tracker)
        elif choice == "8":
            show_statistics_flow(tracker)
        elif choice == "9":
            export_csv_flow(tracker)
        elif choice == "10":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 10.")


if __name__ == "__main__":
    main()