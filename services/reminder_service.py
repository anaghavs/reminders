from datetime import datetime
from domain_models.reminder import Reminder
from persistence.user_repo import UserRepo
from persistence.reminder_repo import ReminderRepo
from persistence.unit_of_work import UnitOfWork


def add_reminder(title: str, due_date: datetime, email: str):

    with UnitOfWork() as uow:
        with uow.get_session() as session:
            user_repo = UserRepo(session=session)
            user = user_repo.get_user_by_email(email=email)
            reminder = Reminder(title=title, due_date=due_date, user=user)
            reminder_repo = ReminderRepo(session=session)
            reminder_repo.add_reminder(reminder)
            session.commit()


def list_reminders():
    with UnitOfWork() as uow:
        with uow.get_session() as session:
            reminder_repo = ReminderRepo(session=session)
            return reminder_repo.list_reminders()
