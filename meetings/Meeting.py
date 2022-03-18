from datetime import datetime


class Meeting:
    def __init__(self, date: datetime, title: str):
        self.date = date
        self.title = title