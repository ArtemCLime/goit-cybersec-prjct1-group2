from bot import Bot

"""
    Main application entry point.

"""

try:
    import rich
except:
    print("can't load rich module")

if __name__ == "__main__":
    # TODO: file should be located in the user homw folder.
    # Be avare Windows and Linux users has different logic for file access
    book_file_path = 'file.json'
    bot = Bot(book_file_path)
    bot.idle()
