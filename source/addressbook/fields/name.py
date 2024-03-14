from addressbook.fields.field import Field

class Name(Field):
    """
        Class for the name field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the name field.

        Methods:
        __eq__: Compare the value of the name field with another name field.
        __str__: Return the string representation of the name field.
    
    """ 
    def __init__(self, value, required=True):
        if not self.validate(value, required):
            raise ValueError(f"Invalid name format {value}.")
        super().__init__(value, required)

    def validate(self, value: str, required: bool) -> bool:
        # Validate if the name is not None, or bad type.
        if not isinstance(value, str):
            return False
        if required and not value:
            return False        
        return True
