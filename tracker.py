from models import JobApplication
from storage import export_to_csv, load_applications, save_applications
from utils import is_non_empty, is_valid_date, is_valid_status


class JobTracker:
    def __init__(self, filename: str = "applications.json") -> None:
        self.filename = filename
        self.applications = load_applications(self.filename)

    def _save(self) -> None:
        save_applications(self.applications, self.filename)

    def generate_id(self) -> int:
        if not self.applications:
            return 1
        return max(app["id"] for app in self.applications) + 1

    def add_application(
        self,
        company: str,
        role: str,
        date_applied: str,
        status: str,
        location: str = "",
        notes: str = ""
    ) -> tuple[bool, str]:
        if not is_non_empty(company):
            return False, "Company name cannot be empty."

        if not is_non_empty(role):
            return False, "Role name cannot be empty."

        if not is_valid_date(date_applied):
            return False, "Invalid date. Please use YYYY-MM-DD."

        if not is_valid_status(status):
            return False, "Invalid status."

        application = JobApplication(
            app_id=self.generate_id(),
            company=company.strip(),
            role=role.strip(),
            date_applied=date_applied.strip(),
            status=status.strip(),
            location=location.strip(),
            notes=notes.strip(),
        )

        self.applications.append(application.to_dict())
        self._save()
        return True, "Application added successfully."

    def view_applications(self) -> list[dict]:
        return self.applications

    def find_by_id(self, app_id: int) -> dict | None:
        for app in self.applications:
            if app["id"] == app_id:
                return app
        return None

    def update_status(self, app_id: int, new_status: str) -> tuple[bool, str]:
        if not is_valid_status(new_status):
            return False, "Invalid status."

        application = self.find_by_id(app_id)
        if application is None:
            return False, "Application not found."

        application["status"] = new_status
        self._save()
        return True, "Status updated successfully."

    def delete_application(self, app_id: int) -> tuple[bool, str]:
        application = self.find_by_id(app_id)
        if application is None:
            return False, "Application not found."

        self.applications.remove(application)
        self._save()
        return True, "Application deleted successfully."

    def search_by_company(self, company_name: str) -> list[dict]:
        return [
            app for app in self.applications
            if company_name.lower() in app["company"].lower()
        ]

    def search_by_role(self, role_name: str) -> list[dict]:
        return [
            app for app in self.applications
            if role_name.lower() in app["role"].lower()
        ]

    def filter_by_status(self, status: str) -> list[dict]:
        return [
            app for app in self.applications
            if app["status"].lower() == status.lower()
        ]

    def get_statistics(self) -> dict:
        stats = {
            "Applied": 0,
            "Interview": 0,
            "Offer": 0,
            "Rejected": 0,
        }

        for app in self.applications:
            status = app["status"]
            if status in stats:
                stats[status] += 1
            else:
                stats[status] = stats.get(status, 0) + 1

        stats["Total"] = len(self.applications)
        return stats

    def export_applications_to_csv(self, filename: str = "applications.csv") -> tuple[bool, str]:
        exported = export_to_csv(self.applications, filename)
        if not exported:
            return False, "No applications available to export."

        return True, f"Applications exported to {filename}."