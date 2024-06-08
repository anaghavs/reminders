from datetime import datetime
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from domain_models.reminder import Reminder

class ReminderRepo:

    def __init__(self, session: Session) -> None:
        self._session = session


    def add_reminder(self, reminder: Reminder) -> None:
        self._session.execute(
            text(
                """
                INSERT INTO  reminders (title, due_date) VALUES (
                    :title,
                    :due_date
                )
                """
            ),
            [{"title": reminder.title, "due_date": reminder.due_date}]
        )
   

    def list_reminders(self) -> List[Reminder]:
        db_results = self._session.execute(
            text(
                """
                SELECT title, due_date
                FROM reminders
                """
            )
        )

        results = []

        for row in db_results:
            reminder = Reminder(title=row.title, due_date= datetime.strptime(row.due_date, "%Y-%m-%d %H:%M:%S"))
            results.append(reminder)

        return results






