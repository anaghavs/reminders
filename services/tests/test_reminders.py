from datetime import datetime
from sqlalchemy import Engine
from services import commands
from services import views
from domain_models.reminder import Reminder

def test_reminders(db_engine: Engine):
    # Arrange
    title = "Abhishek's engagement"
    due_date = datetime(year=2024, month=7, day=7, hour=9, minute=0, second=0)
    reminder = Reminder(title=title, due_date=due_date)

    # Act
    commands.add_reminder(title=title, due_date=due_date)
    reminders = views.list_reminders()

    # Assert
    assert len(reminders) == 1
    assert reminder in reminders