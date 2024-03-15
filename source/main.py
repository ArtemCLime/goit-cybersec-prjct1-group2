from bot import Bot

"""
    Main application entry point.
    All suuported commands located in README.md or type help
"""

try:
    import rich
except:
    print("can't load rich module")

if __name__ == "__main__":
    folder = "data"
    bot = Bot(folder)
    bot.idle()
