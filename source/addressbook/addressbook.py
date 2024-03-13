from addressbook.records import Record
from collections import UserDict
import datetime  

class AddressBook(UserDict):
    def add_record(self, name, *phones, birthday=None):
        record = Record(name, birthday)
        for phone in phones:
            record.add_phone(phone)
        self.data[name] = record

    def get_birthdays_per_week(self):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(days=7)
        birthdays = []
        for record in self.data.values():
            if record.birthday:
                b_day, b_month = record.birthday.value.split('.')[:2]
                if int(b_day) >= today.day and int(b_month) == today.month:
                    birthdays.append(record)
                elif int(b_day) < today.day and int(b_month) == next_week.month:
                    birthdays.append(record)
        return birthdays

    def __str__(self):
        if self.data:
            return "\n".join(str(record) for record in self.data.values())
        else:
            return "No contacts found."
        
    def __init__(self):
        self.records = []

    def to_json(self):
        """ Return a JSON representation of the address book. """
        pass


    
