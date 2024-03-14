from addressbook.fields.field import Field

class Phone(Field):
    """
        Class for the phone field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the phone field.

        Methods:
        validate: Validate the value of the phone field.
    
    """ 
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Invalid phone format {value}. Please provide phone as 10 digits number")
        super().__init__(value) 

    def validate(self, value: str) -> bool:
        if not value.isdigit() or len(value) != 10:
             return False                
        return True
