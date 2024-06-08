from domain_models.reminder import Reminder
from datetime import datetime

def test_reminder_model():

    title = "Abhishek's engagement"
    due_date = datetime(year=2024, month=7, day=7, hour=9, minute=0, second=0)
    reminder1 = Reminder(title=title, due_date=due_date)
    reminder2 = Reminder(title=title, due_date=due_date)

    assert reminder1.title == title
    assert reminder1.due_date == due_date
    assert reminder1 == reminder2


