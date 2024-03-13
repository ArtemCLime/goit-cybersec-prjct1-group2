from addressbook.fields.field import Field

class Email(Field):
    """
        Class for the email field in the address book.
        Inherits from Field.

        Attributes:
        value: The value of the email field.

        Methods:
        validate: Validate the value of the email field.
    
    """ 
    def validate(self, value: str) -> bool:
        # Validate if the email is in the correct format.
        pass
        
        # TODO: Implement the validation of the email field.
