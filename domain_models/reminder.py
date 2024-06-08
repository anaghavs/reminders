from dataclasses import dataclass
from datetime import datetime

@dataclass
class Reminder:
    title: str
    due_date: datetime

