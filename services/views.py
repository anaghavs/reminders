from domain_models.reminder import Reminder
from persistence.reminder_repo import ReminderRepo
from persistence.unit_of_work import UnitOfWork


def list_reminders():
    with UnitOfWork() as uow:
        with uow.get_session() as session:
            reminder_repo = ReminderRepo(session=session)
            return reminder_repo.list_reminders()



