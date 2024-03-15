## Unit-test for the Notebook class
from notebook.notebook import NoteBook
from notebook.notes.note import Note


def test_notebook():
    note_book = NoteBook()
    note_book.add("Note 1", "This is a note.")
    note_book.add("Note 2", "This is another note.")
    note_book.add_tag("Note 1", "important")
    note_book.add_tag("Note 2", "urgent")
    note_book.add_tag("Note 2", "important")
    assert note_book.search_by_tags("important") == [Note("This is a note.")]
    assert note_book.search_by_tags("urgent") == [Note("This is another note.")]
    assert note_book.search_by_tags("not important") == []
    assert note_book.read("Note 1") == Note("This is a note.")
    assert note_book.read("Note 2") == Note("This is another note.")
    note_book.delete("Note 1")
    assert note_book.search_by_tags("important") == []
    assert note_book.search_by_tags("urgent") == [Note("This is another note.")]
    assert note_book.search_by_tags("not important") == []
    print("Notebook class test cases passed.")


def test_notebook_from_json():
    note_book = NoteBook()
    data = {
        "Note 1": {"title": "Note 1", "note": "This is a note.", "tags": ["important"]},
        "Note 2": {
            "title": "Note 2",
            "note": "This is another note.",
            "tags": ["urgent", "important"],
        },
    }
    note_book.from_json(data)
    assert note_book.search_by_tags("important") == [
        Note("This is a note."),
        Note("This is another note."),
    ]
    assert note_book.search_by_tags("urgent") == [Note("This is another note.")]
    assert note_book.search_by_tags("not important") == []
    assert note_book.read("Note 1") == Note("This is a note.")
    assert note_book.read("Note 2") == Note("This is another note.")
    note_book.delete("Note 1")
    assert note_book.search_by_tags("important") == [Note("This is another note.")]
    assert note_book.search_by_tags("urgent") == [Note("This is another note.")]
    assert note_book.search_by_tags("not important") == []
    print("Notebook class from_json test cases passed.")


if __name__ == "__main__":
    test_notebook()
    test_notebook_from_json()
