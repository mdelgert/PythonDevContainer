import time
import sys

def main():
    python_ascii_art = """
     ____        _   _                  _
    |  _ \ _   _| |_| |__   ___  _ __  | |
    | |_) | | | | __| '_ \ / _ \| '_ \ | |
    |  __/| |_| | |_| | | | (_) | | | ||_|
    |_|    \__, |\__|_| |_|\___/|_| |_|(_)
           |___/                          
    """

    print(python_ascii_art)
    print(f"Version: {sys.version}")
    # print("Version 1.0")

    # for i in range(5):
    #     print(f"Hello Python {i + 1}!")
    #     time.sleep(1)

if __name__ == "__main__":
    main()

# This is the main entry point of the script
# It calls the main function to start the program
# The script prints a message to the console every second for 10 seconds
# This is a simple script that demonstrates a basic loop and sleep functionality
# The script can be run directly or imported as a module
# The script is designed to be run in a Python environment
