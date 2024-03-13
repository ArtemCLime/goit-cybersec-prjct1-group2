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
            phone: Phone, a list of phone numbers of the record.
            email: Email, The email of the record.
            address: Address, The address of the record.
            birthday: Birthday, The birthdate of the record.

    """
    def __init__(self, name: str, email: Optional[str] = None, phones: Optional[List[str]] = None, address: Optional[str] = None, birthday: Optional[str] = None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None


    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'
    
    def to_json(self):
        """ Return a JSON representation of the record. """
        pass
        # TODO: Implement the to_json method.
    
    def from_json(self, json: Union[str, dict]):
        """ Set the record from a JSON representation. """
        pass
        # TODO: Implement the from_json method.
    
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
