class Note:
    """
    Class for Note. Storage for notes and tags.
    Attributes:
        note: str : The note
        tags: Set[str] : The tags of the note
    """

    def __init__(self, note: str):
        self.note = note
        self.tags = set()

    def to_json(self):
        """Return a JSON representation of the note."""
        return {"note": self.note, "tags": list(self.tags)}

    @classmethod
    def from_json(cls, data: dict):
        """Load the note from a JSON representation."""
        note = cls(data["note"])
        note.tags = set(data["tags"])
        return note

    def __str__(self):
        """Return a string representation of the note."""
        tags = [f"#{tag}" for tag in self.tags]
        return f"{self.note} | {tags}"

    def __repr__(self):
        """Return a string representation of the note."""
        return self.__str__()
