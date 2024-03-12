from source.addressbook.fields.field import Field

class Address(Field):
    """
        Class for the address field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the address field.

        Methods:
        validate: Validate the value of the address field.
    
    """ 
    def validate(self, value: str) -> bool:
        # Validate if the address is in the correct format.
        pass
        
        # TODO: Implement the validation of the address field.
