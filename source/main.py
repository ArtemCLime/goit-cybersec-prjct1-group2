from bot import Bot
import os

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
    if not os.path.exists(folder):
        print(f"Creating data folder at path {folder}")
        os.makedirs(folder)
    bot = Bot(folder)
    bot.idle()
