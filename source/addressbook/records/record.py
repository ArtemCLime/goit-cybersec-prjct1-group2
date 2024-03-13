from addressbook.fields import Address
from addressbook.fields import Birthday
from addressbook.fields import Email
from addressbook.fields import Name
from addressbook.fields import Phone

from typing import Optional, List, Union

class Record:
    """
        Class for Record in the address book.

        Attributes:
            name: Name, The name of the record.
            phones: Phones, a list of phone numbers of the record.
            emails: Emails, a list of email of the record.
            address: Address, The address of the record.
            birthday: Birthday, The birthdate of the record.

    """
    def __init__(self, name: str, 
                 emails: Optional[List[str]] = None, 
                 phones: Optional[List[str]] = None, 
                 address: Optional[str] = None, 
                 birthday: Optional[str] = None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
        self.emails = [Email(email) for email in emails] if emails else []
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None


    def __str__(self):
        return '{name} | {phones} | {emails}'.format(
            name = self.name,
            phones = "; ".join(self.phones),
            emails = "; ".join(self.emails) 
        )
    
    def to_json(self):
        """ Return a JSONable dictionary of the record. """
        return {
            "phones": [str(p) for p in self.phones],
            "emails": [str(e) for e in self.emails],
            "address": str(self.address),
            "birthday": str(self.birthday)
        }
    
    def from_json(self, json: Union[str, dict]):
        """ Set the record from a JSONable dictionary. """
        self.phones = [Phone(phone) for phone in json["phones"]] if json["phones"] else []
        self.emails = [Email(email) for email in json["emails"]] if json["emails"] else [] 
        self.address = Address(json["address"]) if json["address"] else None
        self.birthday = Birthday(json["birthday"]) if json["birthday"] else None 
    
    # CRUD operations, Create, Read, Update, Delete.
    # TODO Implement the CRUD operations.

    def add(self, field_name: str, value: str):
        """ Add a field to the record. """
        pass

    def read(self, field_name: str):
        """ Read a field from the record. """
        pass

    def update(self, field_name: str, value: str):
        """ Update a field in the record. """
        pass

    def delete(self, field_name: str):
        """ Delete a field from the record. """
        pass

if __name__ == "__main__":
    record = Record('test')
