from dataclasses import dataclass
from datetime import datetime
from domain_models.user import User


# creating model
@dataclass
class Reminder:
    title: str
    due_date: datetime
    user: User
