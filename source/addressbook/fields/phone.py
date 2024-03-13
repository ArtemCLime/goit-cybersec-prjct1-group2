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
    def validate(self, value: str) -> bool:
        # Validate is the phone number is in the correct format.
        pass
        
        # TODO: Implement the validation of the phone field.
