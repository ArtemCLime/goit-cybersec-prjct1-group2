from addressbook.fields.field import Field


class Address(Field):
    """
    Class for the address field in the address book.
    Inherits from Field.

    Attributes:
    value: The value of the address field.

    Methods:
    validate: Validate the value of the address field.

    """

    def __init__(self, value):
        if not self.validate(value):
            raise ValueError(f"Invalid address format {value}.")
        super().__init__(value)

    def validate(self, value: str) -> bool:
        # Validate if the address is in the correct format.
        try:
            if not isinstance(value, str):
                return False
        except ValueError:
            return False
        return True
