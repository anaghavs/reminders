from datetime import datetime
from flask import request
from flask_restful import reqparse, Resource
from pydantic import BaseModel

from services.reminder_service import add_reminder, list_reminders

class ReminderViewModel(BaseModel):
    title: str
    due_date: str


class RemindersResource(Resource):

    def get(self):
        reminders = list_reminders()
        
        reminder_view_models = [
            ReminderViewModel(title=reminder.title, due_date=reminder.due_date.strftime("%Y-%m-%d %H:%M:%S"))
            for reminder in reminders]

        return {
            "reminders": [r.model_dump() for r in reminder_view_models]
        }


    def post(self):
        reminder = ReminderViewModel.model_validate(request.json)
        add_reminder(title=reminder.title, due_date= datetime.strptime(reminder.due_date, "%Y-%m-%d %H:%M:%S"))

        return reminder.model_dump_json()
