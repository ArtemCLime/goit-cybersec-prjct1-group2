from addressbook.fields.field import Field
from datetime import datetime

class Birthday(Field):
    """
        Class for the birthday field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the birthday field.

        Methods:
        validate: Validate the value of the birthday field.    

    """ 
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Invalid birthday format {value}. Please provide birthday in dd.mm.yyyy format")
        super().__init__(value) 

    def validate(self, value: str) -> bool:
        # Validate if the birthday is in the correct format.
        if not isinstance(value, str):
            return False
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            return False        
        return True
