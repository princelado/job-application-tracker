from datetime import datetime


VALID_STATUSES = ["Applied", "Interview", "Offer", "Rejected"]


def is_non_empty(text: str) -> bool:
    return bool(text.strip())


def is_valid_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_status(status: str) -> bool:
    return status in VALID_STATUSES


def normalise_status(status: str) -> str:
    cleaned = status.strip().lower()

    mapping = {
        "applied": "Applied",
        "interview": "Interview",
        "offer": "Offer",
        "rejected": "Rejected",
    }

    return mapping.get(cleaned, "")


def print_applications(applications: list[dict]) -> None:
    if not applications:
        print("\nNo applications found.")
        return

    print("\n" + "=" * 70)
    print("JOB APPLICATIONS")
    print("=" * 70)

    for app in applications:
        print(f"ID:           {app['id']}")
        print(f"Company:      {app['company']}")
        print(f"Role:         {app['role']}")
        print(f"Date Applied: {app['date_applied']}")
        print(f"Status:       {app['status']}")
        print(f"Location:     {app['location'] or 'N/A'}")
        print(f"Notes:        {app['notes'] or 'N/A'}")
        print("-" * 70)


def print_statistics(stats: dict) -> None:
    if not stats:
        print("\nNo statistics available.")
        return

    print("\nAPPLICATION STATISTICS")
    print("-" * 30)
    for status, count in stats.items():
        print(f"{status}: {count}")