from addressbook.fields.field import Field
import re

class Email(Field):
    __regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    """
        Class for the email field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the email field.

        Methods:
        validate: Validate the value of the email field.
    
    """ 

    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Invalid email format {value}")
        super().__init__(value) 

    def validate(self, value: str) -> bool:
        # Validate if the email is in the correct format.
        if not isinstance(value, str):
            return False
        if not re.fullmatch(Email.__regex, value):
            return False        
        return True