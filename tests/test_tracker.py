import os
import unittest

from tracker import JobTracker


class TestJobTracker(unittest.TestCase):
    TEST_FILE = "test_applications.json"

    def setUp(self) -> None:
        self.tracker = JobTracker(self.TEST_FILE)
        self.tracker.applications = []
        self.tracker._save()

    def tearDown(self) -> None:
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_add_application(self) -> None:
        success, message = self.tracker.add_application(
            company="Google",
            role="Junior Python Developer",
            date_applied="2026-03-23",
            status="Applied"
        )

        self.assertTrue(success)
        self.assertEqual(len(self.tracker.applications), 1)
        self.assertEqual(self.tracker.applications[0]["company"], "Google")

    def test_update_status(self) -> None:
        self.tracker.add_application(
            company="Google",
            role="Junior Python Developer",
            date_applied="2026-03-23",
            status="Applied"
        )

        success, message = self.tracker.update_status(1, "Interview")

        self.assertTrue(success)
        self.assertEqual(self.tracker.applications[0]["status"], "Interview")

    def test_delete_application(self) -> None:
        self.tracker.add_application(
            company="Atlassian",
            role="Python Intern",
            date_applied="2026-03-23",
            status="Applied"
        )

        success, message = self.tracker.delete_application(1)

        self.assertTrue(success)
        self.assertEqual(len(self.tracker.applications), 0)

    def test_search_by_company(self) -> None:
        self.tracker.add_application(
            company="Canva",
            role="Backend Developer",
            date_applied="2026-03-23",
            status="Applied"
        )

        results = self.tracker.search_by_company("canva")
        self.assertEqual(len(results), 1)

    def test_invalid_date_rejected(self) -> None:
        success, message = self.tracker.add_application(
            company="Seek",
            role="Junior Developer",
            date_applied="23-03-2026",
            status="Applied"
        )

        self.assertFalse(success)
        self.assertEqual(len(self.tracker.applications), 0)


if __name__ == "__main__":
    unittest.main()