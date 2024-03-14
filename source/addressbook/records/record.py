#### Only for testing
## Before testing uncoment the next 3 lines
#import sys
#import os
#sys.path.append(os.path.dirname(__file__) + '/../../')
####

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
        Methods:
            to_json: return LSONable dictionary
            from_json: Return a JSONable dictionary of the record.
            add: Add a field to the record
            read: Read a field from the record
            update: Update a field in the record
            delete: Delete a field from the record
        Notice:
            field_name for add/read/update/delete method can be:
                1. phone - for Phone field
                2. email - for Email field
                3. address - for address field
                4. birthday - for birthday field
            For field_name address/birthday for update method only new_value required
            For field_name address/birthday for delete method value can be None

    """
    def __init__(self, name: str, 
                 emails: Optional[List[str]] = None, 
                 phones: Optional[List[str]] = None, 
                 address: Optional[str] = None, 
                 birthday: Optional[str] = None):
        self.name = Name(name)
        self.phones = [ Phone(phone) for phone in phones ] if phones else []
        self.emails = [ Email(email) for email in emails ] if emails else []
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None


    def __str__(self):
        return '{name} | {phones} | {emails} | {address} | {birthday} '.format(
            name = self.name,
            phones = "; ".join([ p.value for p in self.phones ]),
            emails = "; ".join([ e.value for e in self.emails ]),
            address = self.address.value,
            birthday = self.birthday.value 
        )
    
    def __validate_params(self, param):
        if param is None or len(param) == 0:
            return False
        return True 
    
    def to_json(self):
        """ Return a JSONable dictionary of the record. """
        return {
            "phones": [str(p) for p in self.phones],
            "emails": [str(e) for e in self.emails],
            "address": str(self.address),
            "birthday": str(self.birthday)
        }
    
    def from_json(self, json: Union[str, dict]):
        """ Create the record from a JSONable dictionary. """
        self.phones = [ Phone(phone) for phone in json["phones"] ] if json["phones"] else []
        self.emails = [ Email(email) for email in json["emails"] ] if json["emails"] else [] 
        self.address = Address(json["address"]) if json["address"] else None
        self.birthday = Birthday(json["birthday"]) if json["birthday"] else None 
    
    # CRUD operations, Create, Read, Update, Delete.
    # TODO Implement the CRUD operations.

    def add(self, field_name: str, value: str):
        """ Add a field to the record. """
        if not self.__validate_params(field_name) or not self.__validate_params(value):
            return "Field_name or value is empty."
        if field_name == 'phone':
            """ Add phone to a record list """
            self.phones.append(Phone(value))
        elif field_name == 'email':
            """ Add email to a record list """
            self.emails.append(Email(value))
        elif field_name == 'address':
            """ Add address string to the record """
            self.address = Address(value)
        elif field_name == 'birthday':
            """ Add birthday date to the record """
            self.birthday = Birthday(value)
        else:
            # TODO: return should be changed to raise
            return 'Unrecognize field name.'

    def read(self, field_name: str):
        """ Read a field from the record. """
        if not self.__validate_params(field_name):
            return "Field_name is empty"
        if field_name == 'phone':
            """ Return a list of record phones """
            return [ p.value for p in self.phones ]
        elif field_name == 'email':
            """ Return a list of record emails """
            return [ e.value for e in self.emails ]
        elif field_name == 'address':
            """ Return address string """
            return self.address.value
        elif field_name == 'birthday':
            """ Return birthday string """
            return self.birthday.value
        else:
            # TODO: return should be changed to raise
            return 'Unrecognize field name.'

    def update(self, field_name: str, old_value: str, new_value: str):
        """ Update a field in the record. """
        if field_name == 'phone' and self.__validate_params(old_value) and self.__validate_params(new_value):
            """ Update phone in a record list """
            for p in self.phones:
                if p.value == old_value:
                    self.phones.remove(p)
                    self.phones.append(Phone(new_value))
        elif field_name == 'email' and self.__validate_params(old_value) and self.__validate_params(new_value):
            """ Update email in a record list """
            for e in self.emails:
                if e.value == old_value:
                    self.emails.remove(e)
                    self.emails.append(Email(new_value))
        elif field_name == 'address' and self.__validate_params(new_value):
            """ Update phone in a record """
            self.address = Address(new_value)
        elif field_name == 'birthday' and self.__validate_params(new_value):
            """ Update phone in a record """
            self.birthday = Birthday(new_value)
        else:
            # TODO: return should be changed to raise
            return 'Unrecognize field name.'

    def delete(self, field_name: str, value: str = None):
        """ Delete a field from the record. """
        if field_name == 'phone' and self.__validate_params(value):
            """ Delete phone from a record list """
            for p in self.phones:
                if p.value == value:
                    self.phones.remove(p)
        elif field_name == 'email' and self.__validate_params(value):
            """ Delete email from a record list """
            for e in self.emails:
                if e.value == value:
                    self.emails.remove(e)
        elif field_name == 'address':
            """ Delete phone from a record """
            self.address = None
        elif field_name == 'birthday':
            """ Delete phone from a record """
            self.birthday = None
        else:
            # TODO: return should be changed to raise
            return 'Unrecognize field name.'


if __name__ == "__main__":
    """ Simple testcases """
    record = Record('test')
    record.from_json(
        {
            "phones": ['1234567890', '0987654321'],
            "emails": ['test_1@goit.com', 'test2@goit.com'],
            "address": "test test test",
            "birthday": "03.04.1995"
        }
    )
    print(record)
    print(record.read('phone'))
    print(record.read('email'))
    print(record.read('birthday'))
    print(record.read('address'))

    record.add('phone', '5555555555')
    print(record.add('phone', None))
    print(record.add('phone', ''))
    record.add('email', 'test3@goit.com')
    print(record) 
    print(record.to_json())

    record.delete('phone', '1234567890')
    record.delete('email', 'test2@goit.com')
    print(record)

    record.update('phone', '5555555555', '6666666666')
    record.update('email', 'test_1@goit.com', 'test5@goit.com')
    record.update('address', None, 'test2 test2 test2')
    record.update('birthday', None, '05.10.1995')

    print(record)