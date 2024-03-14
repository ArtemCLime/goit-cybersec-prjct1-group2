

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
