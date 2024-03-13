from addressbook.records import Record


class AddressBook:
    """
        Class for AddressBook in the address book.

        Attributes:
            records: List[Record], The list of records in the address book.

    """
    def __init__(self):
        self.records = []

    def __str__(self):
        return f'{self.records}'

    def to_json(self):
        """ Return a JSON representation of the address book. """
        pass

    # CRUD operations, Create, Read, Update, Delete.

    def add(self, record: Record):
        """ Add a record to the address book. """
        pass
        # TODO: Implement the add method.

    def read(self, name: str):
        """ Read a record from the address book. """
        pass
        # TODO: Implement the read method.
    
    def update(self, name: str, record: Record):
        """ Update a record in the address book. """
        pass
        # TODO: Implement the update method.
    
    def delete(self, name: str):
        """ Delete a record from the address book. """
        pass
        # TODO: Implement the delete method.

    