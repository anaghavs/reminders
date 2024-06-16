from datetime import datetime
from domain_models.user import User
from domain_models.reminder import Reminder


def test_reminder_model():

    title = "Abhishek's engagement"
    due_date = datetime(year=2024, month=7, day=7, hour=9, minute=0, second=0)
    user = User(name="Anagha Shenoy", email="anagha.1512@gmailcom", password_hash="1234")
    
    reminder1 = Reminder(title=title, due_date=due_date, user=user)
    reminder2 = Reminder(title=title, due_date=due_date, user=user)

    assert reminder1.title == title
    assert reminder1.due_date == due_date
    assert reminder1.user == user
    assert reminder1 == reminder2


