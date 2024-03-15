class Field:
    """
    Base class for all fields in the address book.
    All fields should inherit from this class.

    Attributes:
    value: The value of the field.

    Methods:
    __eq__: Compare the value of the field with another field.
    __str__: Return the string representation of the field.

    """

    def __init__(self, value, required=False):
        self.value = value
        self.is_required = required

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __str__(self) -> str:
        return str(self.value)

    def validate(self, value) -> bool:
        return True
