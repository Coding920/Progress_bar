# Progress bar module for import to your command line project, simply feed it the precent during a loading loop

EMPTY_CHAR = "*"
FULL_CHAR = "="
HEAD_CHAR = ">"

class ProgressBar:
    def __init__(self, empty_char = EMPTY_CHAR, full_char = FULL_CHAR, head_char = HEAD_CHAR):
        self.empty_char = empty_char
        self.full_char = full_char
        self.head_char = head_char

    def display(self, filled, full_size, message):
        print(message, end="\033[0J \033[1B \r")
        print("[" + self.full_char * (filled - 1) + self.head_char + self.empty_char * (full_size - filled) + "]", end="\033[1A \r")

    def prep(self):
        print("\033[?25l", end="")

    def end_display(self):
        print("\033[?25h")
        print()
