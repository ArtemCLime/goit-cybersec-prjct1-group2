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

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phone_str = '; '.join(str(p) for p in self.phones)
        if self.birthday:
            return f"Contact name: {self.name.value}, phones: {phone_str}, birthday: {self.birthday}"
        else:
            return f"Contact name: {self.name.value}, phones: {phone_str}"
