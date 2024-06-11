from dataclasses import dataclass
from datetime import datetime


# creating model
@dataclass
class Reminder:
    title: str
    due_date: datetime

