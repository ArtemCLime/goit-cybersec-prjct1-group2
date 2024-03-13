from bot import Bot

"""
    Main application entry point.

"""

try:
    import rich
except:
    print("can't load rich module")

if __name__ == "__main__":
    bot = Bot()
    bot.idle()
