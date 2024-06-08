from datetime import datetime
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from domain_models.reminder import Reminder
from persistence.reminder_repo import ReminderRepo


def test_reminder_repo(db_engine: Engine) -> None:
    reminder1_title = "Abhishek's engagement"
    reminder1_date = datetime(year=2024, month=7, day=7, hour=9, minute=0)

    reminder2_title = "Abhishek's wedding"
    reminder2_date = datetime(year=2024, month=11, day=17, hour=12, minute=34)

    reminder1 = Reminder(title=reminder1_title, due_date=reminder1_date)
    reminder2 = Reminder(title=reminder2_title, due_date=reminder2_date)

    
    with Session(db_engine) as session:
        reminder_repo = ReminderRepo(session=session)
        reminder_repo.add_reminder(reminder=reminder1)
        reminder_repo.add_reminder(reminder=reminder2)
        session.commit()
    
    with Session(db_engine) as session:
        reminder_repo = ReminderRepo(session=session)
        reminders = reminder_repo.list_reminders()

        assert reminder1 in reminders
        assert reminder2 in reminders
        assert len(reminders) == 2

