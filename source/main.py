import os
from bot import Bot

"""
    Main application entry point.
    All suuported commands located in README.md or type help
"""

def main():
    folder = "data"
    if not os.path.exists(folder):
        print(f"Creating data folder at path {folder}")
        os.makedirs(folder)
    bot = Bot(folder)
    bot.idle() 

try:
    import rich
except:
    print("can't load rich module")

if __name__ == "__main__":
    folder = "data"
    bot = Bot(folder)
    bot.idle()
