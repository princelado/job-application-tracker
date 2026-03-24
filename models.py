class JobApplication:
    def __init__(
        self,
        app_id: int,
        company: str,
        role: str,
        date_applied: str,
        status: str,
        location: str = "",
        notes: str = ""
    ) -> None:
        self.id = app_id
        self.company = company
        self.role = role
        self.date_applied = date_applied
        self.status = status
        self.location = location
        self.notes = notes

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "company": self.company,
            "role": self.role,
            "date_applied": self.date_applied,
            "status": self.status,
            "location": self.location,
            "notes": self.notes,
        }