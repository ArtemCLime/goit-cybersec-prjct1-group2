from addressbook.fields.field import Field


class Birthday(Field):
    """
        Class for the birthday field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the birthday field.

        Methods:
        validate: Validate the value of the birthday field.
    
    """ 
    def validate(self, value: str) -> bool:
        # Validate if the birthday is in the correct format.
        pass
        
        # TODO: Implement the validation of the birthday field.
