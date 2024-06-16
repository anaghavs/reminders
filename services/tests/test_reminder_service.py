from datetime import datetime
from sqlalchemy import Engine
from sqlalchemy.orm import Session


from domain_models.user import User
from domain_models.reminder import Reminder

from persistence.user_repo import UserRepo
from services import reminder_service, user_service

def test_reminders(db_engine: Engine):


    user_service.register_user(name="Anagha Shenoy", email="anagha.1512@gmail.com", password="N0t@R3@lP@$$w0rd")
    user = user_service.get_user_by_email(email="anagha.1512@gmail.com")

    title = "Abhishek's engagement"
    due_date = datetime(year=2024, month=7, day=7, hour=9, minute=0, second=0)
    reminder = Reminder(title=title, due_date=due_date, user=user)

    # Act
    reminder_service.add_reminder(title=title, due_date=due_date, email="anagha.1512@gmail.com")
    reminders = reminder_service.list_reminders_by_user(email=user.email)

    # Assert
    assert len(reminders) == 1
    assert reminder in reminders