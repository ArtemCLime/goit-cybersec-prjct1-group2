from typing import Union, List
from addressbook import AddressBook
from notebook.notes import Note
from search.search import search


class NoteBook(AddressBook):
    """
    Class for Note Book. Storage for notes and tags.
    Attributes:
        self.data: Dict[str, Note] : The data of the note book

    """

    def from_json(self, data: Union[str, dict]):
        """Load the address book from a JSON representation."""
        self.data = {title: Note.from_json(note) for title, note in data.items()}

    # CRUD operations, Create, Read, Update, Delete.
    def add(self, title: str, note: str):
        """Add a note to the address book."""
        self.data[title] = Note(note)

    def read(self, title: str):
        """Read a note from the address book."""
        return str(self.data.get(title))

    def update(self, title: str, note: Note):
        """Update a note in the address book."""
        self.data[title] = Note(note)

    def delete(self, title: str):
        """Delete a note from the address book."""
        del self.data[title]

    def add_tag(self, title: str, tag: str):
        """Add a tag to the note."""
        self.data[title].tags.add(tag)

    def remove_tag(self, title: str, tag: str):
        """Remove a tag from the note."""
        self.data[title].tags.remove(tag)

    def search_by_tags(self, tags: List[str]):
        """Search for a tag in the note book."""
        return [note for note in self.data.values() if any(tag in note.tags for tag in tags)]

    def search_by_text(self, query: str):
        """Search for a text query in the note book.
        Returns maximum top-3 matching notes.
        """
        return search(query, [i.note for i in self.data.values()], top_n=3)
