import unittest
from unittest.mock import patch
from bot import Bot

class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot = Bot("test_data")

    def test_add_contact(self):
        result = self.bot.add_contact(["John", "1234567890"])
        self.assertEqual(result, "Contact added.")

    def test_add_contact_invalid_args(self):
        result = self.bot.add_contact(["John"])
        self.assertEqual(result, "You need to provide exactly 2 argument(s) to add_contact.")

    def test_add_field(self):
        self.bot.add_contact(["John", "1234567890"])
        result = self.bot.add_field(["John", "email", "john@example.com"])
        self.assertEqual(result, "Field added.")

    def test_add_field_invalid_args(self):
        result = self.bot.add_contact(["John", "1234567890"])
        result = self.bot.add_field(["John", "email"])
        self.assertEqual(result, "You need to provide exactly 3 argument(s) to add_field.")

    def test_update_contact(self):
        self.bot.add_contact(["John", "1234567890"])
        result = self.bot.update_contact(["John", "phone", "1234567890", "9876543210"])
        self.assertEqual(result, "Contact updated.")

    def test_update_contact_invalid_args(self):
        result = self.bot.update_contact(["John", "phone", "1234567890"])
        self.assertEqual(result, "You need to provide exactly 4 argument(s) to update_contact.")

    def test_show_phone(self):
        self.bot.add_contact(["John", "1234567890"])
        result = self.bot.show_phone(["John"])
        self.assertEqual(result, ["1234567890"])

    def test_show_all_contacts(self):
        self.bot.add_contact(["John", "1234567890"])
        self.assertEqual(self.bot.show_all_contacts(), "John | 1234567890 |  | None | None ")

    def test_add_birthday(self):
        self.bot.add_contact(["John", "1234567890"])
        result = self.bot.add_birthday(["John", "01.01.2001"])
        self.assertEqual(result, "Birthday added.")

    def test_add_birthday_invalid_args(self):
        self.bot.add_contact(["John", "1234567890"])
        result = self.bot.add_birthday(["John"])
        self.assertEqual(result, "You need to provide exactly 2 argument(s) to add_birthday.")

    def test_show_birthday(self):
        self.bot.add_contact(["John", "1234567890"])
        self.bot.add_birthday(["John", "01.01.2001"])
        result = self.bot.show_birthday(["John"])
        self.assertEqual(result, "01.01.2001")

    def test_search_by_field(self):
        self.bot.add_contact(["John", "1234567890"])
        self.bot.add_field(["John", "email", "john@example.com"])
        result = self.bot.search_by_field(["email", "john@example.com"])
        self.assertEqual(result, "John | 1234567890 | john@example.com | None | None ")

    def test_search_by_field_invalid_args(self):
        result = self.bot.search_by_field(["email"])
        self.assertEqual(result, "You need to provide exactly 2 argument(s) to search_by_field.")

    def test_book_save(self):
        result = self.bot.book_save()
        self.assertEqual(result, "Book saved.")

    def test_load_book(self):
        result = self.bot.load_book()
        self.assertEqual(result, "Book loaded.")

    def test_add_note(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
            self.assertEqual(result, "Note added.")

    def test_add_note_invalid_args(self):
        result = self.bot.add_note([])
        self.assertEqual(result, "You need to provide exactly 1 argument(s) to add_note.")

    def test_edit_note(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        with patch("builtins.input", return_value="This is an updated note."):
            result = self.bot.edit_note(["Note 1"])
            self.assertEqual(result, "Note updated.")

    def test_edit_note_invalid_args(self):
        result = self.bot.edit_note([])
        self.assertEqual(result, "You need to provide exactly 1 argument(s) to edit_note.")

    def test_delete_note(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        result = self.bot.delete_note(["Note 1"])
        self.assertEqual(result, "Note deleted.")

    def test_delete_note_invalid_args(self):
        result = self.bot.delete_note([])
        self.assertEqual(result, "You need to provide exactly 1 argument(s) to delete_note.")

    def test_add_note_tags(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        result = self.bot.add_note_tags(["Note 1", "important", "urgent"])
        self.assertEqual(result, "Tags added.")

    def test_remove_note_tags(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        result = self.bot.add_note_tags(["Note 1", "important", "urgent"])
        result = self.bot.remove_note_tags(["Note 1", "important"])
        self.assertEqual(result, "Tags removed.")

    def test_show_note(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        result = self.bot.add_note_tags(["Note 1", "important"])
        result = self.bot.show_note(["Note 1"])
        self.assertEqual(result, "This is a note. | ['#important']")

    def test_show_note_invalid_args(self):
        result = self.bot.show_note([])
        self.assertEqual(result, "You need to provide exactly 1 argument(s) to show_note.")

    def test_wrong_input(self):
        result = self.bot.wrong_input("addd")
        self.assertEqual(result, "Invalid command. Did you mean 'add'?")

    def test_search_note(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        result = self.bot.search_note(["note"])
        self.assertEqual(result, ["This is a note."])

    def test_search_note_tags(self):
        with patch("builtins.input", return_value="This is a note."):
            result = self.bot.add_note(["Note 1"])
        result = self.bot.add_note_tags(["Note 1", "important"])
        result = self.bot.search_note(["tags:", "important"])
        self.assertEqual(result[0].note, "This is a note.")

if __name__ == "__main__":
    unittest.main()
