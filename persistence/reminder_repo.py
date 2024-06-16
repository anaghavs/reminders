from datetime import datetime
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from domain_models.user import User
from domain_models.reminder import Reminder

class ReminderRepo:

    def __init__(self, session: Session) -> None:
        self._session = session


    def add_reminder(self, reminder: Reminder) -> None:
        self._session.execute(
            text(
                """
                INSERT INTO  reminders (title, due_date, user_id) VALUES (
                    :title,
                    :due_date,
                    (SELECT id FROM users where email=:user_email)
                )
                """
            ),
            [{"title": reminder.title, "due_date": reminder.due_date, "user_email": reminder.user.email}]
        )
   

    def list_reminders(self) -> List[Reminder]:
        db_results = self._session.execute(
            text(
                """
                SELECT reminders.title as title, reminders.due_date as due_date, users.name as name, users.email as email, users.password_hash as password_hash
                FROM reminders INNER JOIN users
                where reminders.user_id = users.id
                """
            )
        )

        results = []

        for row in db_results:
            user = User(name=row.name, email=row.email, password_hash=row.password_hash)
            reminder = Reminder(title=row.title, due_date= datetime.strptime(row.due_date, "%Y-%m-%d %H:%M:%S"), user=user)
            results.append(reminder)

        return results






