from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder:
    EMAIL: ClassVar[str] = "email"
    SYSTEM: ClassVar[str] = "system"

    date_time: datetime
    type: str = EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"

# TODO: Implement Event class here
@dataclass
class Event:
    title: str
    description: str
    date_: date
    star_at: datetime
    end_at: time
    reminders: list[Reminder] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_reminder(self, date_time: datetime, type: str):
        reminder = Reminder(date_time, type)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if self.reminders[reminder_index]:
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self):
        pass

# TODO: Implement Calendar class here

from datetime import date, time
from typing import Dict, Optional


class Day:
    def __init__(self, date_: date):
        self.date_ = date_
        self.slots: Dict[time, Optional[str]] = {}
        self._init_slots()

    def _init_slots(self):
        pass
